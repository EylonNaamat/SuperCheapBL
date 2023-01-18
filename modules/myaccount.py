import requests

class MyAccount:
    def __init__(self,user) -> None:
        self.user = user
    
    def change_user(self):
        URL = "http://172.17.0.3:8000/myaccount/setuser"
        
        r = requests.get(url = URL, params=self.user)
        data = r.json()
        return data
    