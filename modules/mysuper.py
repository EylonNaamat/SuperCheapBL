import requests

class MySuper:
    def __init__(self,Super_Id) -> None:
        self.Super_Id = Super_Id

    def get_super(self):
        URL = "http://172.17.0.3:8000/mysuper/getsuper"
        PARAM = {"Super_Id":self.Super_Id}

        r = requests.get(url = URL, params=PARAM)
        data = r.json()
        return data
    
    def set_super(self,super_name:str, super_city:str):
        URL = "http://172.17.0.3:8000/mysuper/setsuper"
        PARAM = {"Super_Id":self.Super_Id, "super_name":super_name , "super_city":super_city}

        r = requests.get(url = URL, params=PARAM)
        data = r.json()
        return data

    def moveSuper(self, old_city:str,new_city:str):
        URL = "http://172.17.0.3:8000/mysuper/movesuper"
        PARAM = {"old_city":old_city, "new_city":new_city, "Super_Id":self.Super_Id}
        
        r = requests.get(url = URL, params=PARAM)
        data = r.json()
        return data
