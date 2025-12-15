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

    @staticmethod
    def find_latest_directory(base_path: str, contain: str) -> str | None:
        dirs = [
            f"{base_path}/{d}"
            for d in os.listdir(base_path)
            if os.path.isdir(f"{base_path}/{d}") and contain in d
        ]
        if not dirs:
            return None
        latest_dir = max(dirs, key=os.path.getmtime)
        return latest_dir
