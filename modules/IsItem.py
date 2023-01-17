import requests


class IsItem:
    def __init__(self, item:dict) -> None:
        self.item = item

    def get_isitem(self):
        URL = "http://172.17.0.3:8000/isitem"

        r = requests.get(url = URL, params=self.item)

        data = r.json()

        return data