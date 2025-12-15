import time

from src.commons.data_manager import DataManager
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
import torch

import os
import matplotlib.pyplot as plt


class TrainTextModel:

    def __init__(self):
        self.tokenizer = None
        self.model = None
        self.inputs = []
        self.train_data = []
        self.val_data = []
        self.dataset = []

    def load_dataset(self):
        dataset_path = DataManager.ls_directory("dataset")
        dataset = []
        for file_name in dataset_path:
            if file_name.endswith(".json"):
                data = DataManager.load_json(f"dataset/{file_name}")
                dataset.extend(data)
        self.dataset = dataset

    def load_model(self):
        model_name = "distilgpt2"  # "huggyllama/llama-7b"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model.config.pad_token_id = self.tokenizer.eos_token_id

    def tokenize_dataset(self):

        for article in self.dataset:
            text = article["title"] + "\n" + article["content"]
            tokenized = self.tokenizer(
                text,
                return_tensors="pt",
                truncation=True,
                padding="max_length",
                max_length=512,
            )
            self.inputs.append(tokenized)

    def split_dataset(self):
        split_idx = int(0.8 * len(self.inputs))
        self.train_data = self.inputs[:split_idx]
        self.val_data = self.inputs[split_idx:]

    @staticmethod
    def data_collator(features):
        batch = {}
        batch["input_ids"] = torch.stack(
            [torch.tensor(f["input_ids"]) for f in features]
        )
        batch["attention_mask"] = torch.stack(
            [torch.tensor(f["attention_mask"]) for f in features]
        )
        batch["labels"] = batch["input_ids"].clone()
        return batch

    @staticmethod
    def graph_data(trainer, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        history = trainer.state.log_history
        loss_entries = [h for h in history if "loss" in h]
        if loss_entries:
            steps = [h.get("step", i) for i, h in enumerate(loss_entries)]
            losses = [h["loss"] for h in loss_entries]
            plt.figure()
            plt.plot(steps, losses, marker="o")
            plt.xlabel("step")
            plt.ylabel("loss")
            plt.title("Training loss")
            plt.savefig(os.path.join(output_dir, "training_loss.png"))
            plt.close()

    def run(self, epochs: int = 3, lr: float = 5e-5):
        output_dir = f"./models/text-model-finetuned_{time.strftime('%Y-%m-%d-%H-%M')}"
        self.load_dataset()
        self.load_model()
        self.tokenize_dataset()
        self.split_dataset()
        training_args = TrainingArguments(
            output_dir=output_dir,
            learning_rate=lr,
            per_device_train_batch_size=2,
            per_device_eval_batch_size=2,
            num_train_epochs=epochs,
            weight_decay=0.01,
            logging_steps=10,
            save_strategy="epoch",
            # use_cpu=True,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=self.train_data,
            eval_dataset=self.val_data,
            data_collator=self.data_collator,
        )

        trainer.train()

        self.graph_data(trainer, output_dir)

        trainer.save_model(output_dir)

        self.tokenizer.save_pretrained(output_dir)


if __name__ == "__main__":
    trainer = TrainTextModel()
    trainer.run(epochs=30, lr=5e-5)
