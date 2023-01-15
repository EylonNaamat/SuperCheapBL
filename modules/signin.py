import requests

class SignIn:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def dosighin(self):
        print("1")
        URL = "http://172.17.0.3:8000/signin/getuser"
        PARAM = {"username":self.username,"password":self.password}
        r = requests.get(url = URL, params=PARAM)
        print("2")
        data = r.json()
        print("3")
        return data


#  http://localhost:5000/signin?username=amit24105&password="12345"