import requests

class SignIn:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def dosighin(self):
        URL = "http://172.17.0.3:8000/signin/getuser"

        PARAM = {"username":self.username,"password":self.password}
        
        r = requests.get(url = URL, params=PARAM)
        data = r.json()
        return data


#  http://localhost:5000/signin?username=amit24105&password="12345"