import requests

class SignUp:
    def __init__(self, user:dict, new_super:dict) -> None:
        self.user = user
        self.my_super = new_super

    def insert_user(self):
        is_exists = self.check_user_exists()

        if is_exists["user"] == "exists":
            return is_exists
        else:
            insertion_status = self.insert_user_to_fb()
            return insertion_status

    def check_user_exists(self):
        URL = "http://172.17.0.3:8000/signup/user/checkuserexists"

        PARAM = {"username":self.user["username"]}
        r = requests.get(url = URL, params=PARAM)

        data = r.json()

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

        PARAMS = {'super_ID':self.my_super["super_ID"], 'super_city':self.my_super["super_city"]}

        r = requests.get(url = URL, params=PARAMS)

        data = r.json()

        return data
