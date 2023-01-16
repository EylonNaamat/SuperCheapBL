import requests


class DeleteItem:
    def __init__(self, item:dict) -> None:
        self.item = item

    def delete_item_from_DB(self):
        URL = "http://172.17.0.3:8000/deleteitem"

        r = requests.get(url = URL, params=self.item)

        data = r.json()

        return data
