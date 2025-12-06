import os
import json


class DataManager:

    @staticmethod
    def create_directory(path: str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def load_json(file_path: str):
        with open(file_path, "r") as file:
            return json.load(file)

    @staticmethod
    def save_json(data, file_path: str) -> None:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def ls_directory(path: str):
        return os.listdir(path)

    @staticmethod
    def exists_directory(path: str) -> bool:
        return os.path.exists(path) and os.path.isdir(path)
