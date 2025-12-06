import requests
from io import BytesIO
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms


class ImageDataset(Dataset):
    def __init__(self, dataset, tokenizer, image_size=512):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.image_size = image_size

        self.preprocess = transforms.Compose(
            [
                transforms.Resize((image_size, image_size)),
                transforms.ToTensor(),
                transforms.Normalize([0.5], [0.5]),
            ]
        )

        self.images = []
        self.prompts = []

        self._load_images()

    def _load_images(self):
        for item in self.dataset:
            prompt = item["title"] + " " + item["content"]

            for url in item["pictures_urls"]:
                try:
                    response = requests.get(url, timeout=10)
                    img = Image.open(BytesIO(response.content)).convert("RGB")
                    img = self.preprocess(img)
                    self.images.append(img)
                    self.prompts.append(prompt)
                except Exception as e:
                    print(f"[WARNING] Failed to load image: {url} — {e}")

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        text_inputs = self.tokenizer(
            self.prompts[idx],
            padding="max_length",
            max_length=77,
            truncation=True,
            return_tensors="pt",
        )

        return {
            "pixel_values": self.images[idx],
            "input_ids": text_inputs.input_ids[0],
            "attention_mask": text_inputs.attention_mask[0],
        }
