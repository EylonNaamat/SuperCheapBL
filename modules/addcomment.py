import requests

class AddComment:
    def __init__(self,comment) -> None:
        self.comment = comment

    def addCommentToDataBase(self):
        URL = "http://172.17.0.3:8000/addcomment"
        
        r = requests.get(url = URL, params=self.comment)
        data = r.json()
        return data
    