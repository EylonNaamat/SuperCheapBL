import requests


class DoSale:
    def __init__(self, item:dict) -> None:
        self.item = item

    def insert_sale_to_FB(self):
        URL = "http://172.17.0.3:8000/dosale"

        r = requests.get(url = URL, params=self.item)

        data = r.json()

        return data

