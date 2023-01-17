import requests


class IsCity:
    def __init__(self, city:dict) -> None:
        self.city = city

    def get_iscity(self):
        URL = "http://172.17.0.3:8000/iscity"

        r = requests.get(url = URL, params=self.city)

        data = r.json()

        return data