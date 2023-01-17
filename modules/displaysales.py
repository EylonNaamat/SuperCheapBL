import requests

class DisplaySales:
    def __init__(self,super_details) -> None:
        self.super_details = super_details

    def getSalesfromDataBase(self):
        URL = "http://172.17.0.3:8000/displaysale"
        r = requests.get(url = URL, params=self.super_details)
        data = r.json()
        return data
    