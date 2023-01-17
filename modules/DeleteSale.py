import requests


class DeleteSale:
    def __init__(self, sale:dict) -> None:
        self.sale = sale

    def delete_sale_from_FB(self):
        URL = "http://172.17.0.3:8000/deletesale"

        r = requests.get(url = URL, params=self.sale)

        data = r.json()

        return data
