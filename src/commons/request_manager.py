import requests


class RequestManager:

    @staticmethod
    def get(url: str, headers: dict = None, params: dict = None):
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.text
