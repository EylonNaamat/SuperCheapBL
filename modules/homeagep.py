import requests

class HomePage:
    def __init__(self,details) -> None:
        self.details = details

    def getcomments(self):
        URL = "http://172.17.0.3:8000/getnewcomments"
        r = requests.get(url = URL, params=self.details)
        data = r.json()

        counter = 0
        text_data = {}
        
        if data is None:
            return {"numberOfNew":0}

        for key ,val in data.items():
            counter = counter +1

            URL = "http://172.17.0.3:8000/getcomment"
            coment_r = requests.get(url = URL, params={"id_comment":val.get("id_comment"),"super_ID":self.details.get("super_ID")})
            coment_data = coment_r.json()

            username = coment_data.get("user_username")
            grade = coment_data.get("grade")
            review = coment_data.get("review")
            text = f"username:{username}\n grade:{grade}\n review:{review}"

            text_data[counter] = text

        text_data["numberOfNew"] = counter
        return text_data
    