from src.commons.data_manager import DataManager
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
import torch


class TrainTextModel:

    def __init__(self):
        self.tokenizer = None
        self.model = None
        self.inputs = []
        self.train_data = []
        self.val_data = []
        self.dataset = []  # list of dict with "title" and "content" keys

    def load_dataset(self):
        dataset_path = DataManager.ls_directory("dataset")
        dataset = []
        for file_name in dataset_path:
            if file_name.endswith(".json"):
                data = DataManager.load_json(f"dataset/{file_name}")
                dataset.extend(data)
        self.dataset = dataset

    def load_model(self):
        model_name = "distilgpt2"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model.config.pad_token_id = self.tokenizer.eos_token_id

    def tokenize_dataset(self):

        for article in self.dataset:
            text = article["title"] + "\n" + article["content"]
            tokenized = self.tokenizer(text, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
            self.inputs.append(tokenized)

    def split_dataset(self):
        split_idx = int(0.8 * len(self.inputs))
        self.train_data = self.inputs[:split_idx]
        self.val_data = self.inputs[split_idx:]

    @staticmethod
    def data_collator(features):
        batch = {}
        batch["input_ids"] = torch.stack([torch.tensor(f["input_ids"]) for f in
                                          features])
        batch["attention_mask"] = torch.stack([torch.tensor(f["attention_mask"]) for f
                                               in features])
        batch["labels"] = batch["input_ids"].clone()
        return batch

    def run(self, epochs: int = 3, lr: float = 5e-5):
        output_dir = "./mini-gpt-finetuned"
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
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=self.train_data,
            eval_dataset=self.val_data,
            data_collator=self.data_collator,
        )

        trainer.train()

        trainer.save_model(output_dir)
        self.tokenizer.save_pretrained(output_dir)


if __name__ == "__main__":
    trainer = TrainTextModel()
    trainer.run(epochs=30, lr=5e-5)
