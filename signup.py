import requests

class SignUp:
    def __init__(self, user:dict, new_super:dict) -> None:
        self.user = user
        self.my_super = new_super

    def check_user_exists(self):
        print("enter2")
        URL = "http://172.17.0.3:8000/signup/user/checkuserexists"

        PARAM = {"username":self.user["username"]}
        r = requests.get(url = URL, params=PARAM)
        print("get respone")

        data = r.json()
        print(f"data is {data}")

        return data

    def insert_user_to_fb(self):
        URL = "http://172.17.0.3:8000/signup/user/insertuser"

        r = requests.get(url = URL, params=self.user)

        data = r.json()

        return data

    def insert_super_to_fb(self):
        URL = "http://172.17.0.3:8000/signup/super/insertsuper"

        r = requests.get(url = URL, params=self.my_super)

        data = r.json()

        return data

    def insert_city_to_fb(self):
        URL = "http://172.17.0.3:8000/signup/city/insertcity"

        r = requests.get(url = URL, params=self.my_super)

        data = r.json()

        return data
