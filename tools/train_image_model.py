import os
from diffusers import StableDiffusionPipeline, DDPMScheduler
from diffusers.optimization import get_scheduler
import torch
from torch.utils.data import DataLoader

from src.commons.data_manager import DataManager
from src.commons.image_dataset import ImageDataset


class TrainImageModel:

    def __init__(self):
        self.dataset = []
        self.train_dataset = None
        self.val_dataset = None

        self.tokenizer = None
        self.pipeline = None
        self.unet = None
        self.noise_scheduler = None

    def load_dataset(self):
        dataset_path = DataManager.ls_directory("dataset")
        dataset = []
        for file_name in dataset_path:
            if file_name.endswith(".json"):
                data = DataManager.load_json(f"dataset/{file_name}")
                dataset.extend(data)
        self.dataset = dataset

    def load_model(self):
        model_name = "runwayml/stable-diffusion-v1-5"

        self.pipeline = StableDiffusionPipeline.from_pretrained(
            model_name,
            torch_dtype=torch.float32
        )

        self.tokenizer = self.pipeline.tokenizer
        self.unet = self.pipeline.unet
        self.noise_scheduler = DDPMScheduler.from_config(self.pipeline.scheduler.config)

    def tokenize_and_prepare_dataset(self):
        dataset = ImageDataset(self.dataset, self.tokenizer)
        split = int(0.8 * len(dataset))
        self.train_dataset = torch.utils.data.Subset(dataset, range(0, split))
        self.val_dataset = torch.utils.data.Subset(dataset, range(split, len(dataset)))

    def train(self, epochs=5, lr=1e-5, batch_size=2, out_dir="./image-model-finetuned"):

        self.load_dataset()
        self.load_model()
        self.tokenize_and_prepare_dataset()

        train_loader = DataLoader(self.train_dataset, batch_size=batch_size, shuffle=True)

        optimizer = torch.optim.AdamW(self.unet.parameters(), lr=lr)

        lr_scheduler = get_scheduler(
            "linear",
            optimizer=optimizer,
            num_warmup_steps=500,
            num_training_steps=len(train_loader) * epochs,
        )

        device = "cpu"  # sorry but no have a lot of VRAM

        self.unet.to(device)
        self.pipeline.text_encoder.to(device)
        self.pipeline.vae.to(device)

        global_step = 0

        for epoch in range(epochs):
            for batch in train_loader:
                optimizer.zero_grad()

                pixel_values = batch["pixel_values"].to(device)
                input_ids = batch["input_ids"].to(device)
                attention_mask = batch["attention_mask"].to(device)

                # --- Encode image to 4-channel latents ---
                with torch.no_grad():
                    latents = self.pipeline.vae.encode(pixel_values).latent_dist.sample()
                    latents = latents * self.pipeline.vae.config.scaling_factor

                # Create noise
                noise = torch.randn_like(latents).to(device)

                # Random timesteps
                timesteps = torch.randint(
                    0,
                    self.noise_scheduler.config.num_train_timesteps,
                    (latents.size(0),),
                    device=device
                ).long()

                noisy_latents = self.noise_scheduler.add_noise(latents, noise, timesteps)

                # Encode text
                encoder_hidden_states = self.pipeline.text_encoder(
                    input_ids=input_ids,
                    attention_mask=attention_mask
                )[0]

                # Predict noise with UNet
                model_pred = self.unet(noisy_latents, timesteps, encoder_hidden_states).sample

                loss = torch.nn.functional.mse_loss(model_pred, noise)
                loss.backward()
                optimizer.step()
                lr_scheduler.step()

                global_step += 1
                if global_step % 10 == 0:
                    print(f"Epoch {epoch} | Step {global_step} | Loss {loss.item():.4f}")

        DataManager.create_directory(out_dir)
        self.unet.save_pretrained(os.path.join(out_dir, "unet"))
        self.tokenizer.save_pretrained(out_dir)

        print(f"Model saved in {out_dir}")


if __name__ == "__main__":
    trainer = TrainImageModel()
    trainer.train(epochs=1, lr=1e-5)
