from typing import Union
import requests
from fastapi import FastAPI
import sched, time
from threading import Thread
import asyncio
from signup import SignUp

app = FastAPI()


# http://localhost:5000/
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# http://localhost:5000/test
@app.get("/test")
def read_root():
    return {"Hello": "test"}

# http://localhost:5000/signup/user?first_name=eylon&last_name=naamat&email=emailll&username=test&password=getPassword&city=getCity&birth_date=getBirth_date&gender=getGender&is_manager=michael&super_id=getSuper_id
@app.get("/signup/user")
async def get_user(first_name:str, last_name:str, email:str, username:str, password:str, city:str, birth_date:str, gender:str, is_manager:str, super_id:str):

    USER = {'first_name':first_name, 'last_name':last_name, 'email':email, 'username':username,
    'password':password, 'city':city, 'birth_date':birth_date, 'gender':gender, 'is_manager':is_manager,
    'super_id':super_id}
    
    sign_up = SignUp(USER, {})

    is_exists = sign_up.check_user_exists()

    if is_exists["user"] == "exists":
        return is_exists
    else:
        insertion_status = sign_up.insert_user_to_fb()
        return insertion_status

# http://localhost:5000/signup/super?super_ID=123456&super_name=hatzlaha&super_city=Ariel
@app.get("/signup/super")
async def get_super(super_ID:str, super_name:str, super_city:str):
    SUPER = {'super_ID':super_ID, 'super_name':super_name, 'super_city':super_city}
    
    sign_up = SignUp({}, SUPER)

    insertion_status = sign_up.insert_super_to_fb()

    return insertion_status

# http://localhost:5000/signup/city?super_ID=123456&super_name=hatzlaha&super_city=Ariel
@app.get("/signup/city")
async def get_super(super_ID:str, super_name:str, super_city:str):
    SUPER = {'super_ID':super_ID, 'super_name':super_name, 'super_city':super_city}
    
    sign_up = SignUp({}, SUPER)

    insertion_status = sign_up.insert_city_to_fb()
    
    return insertion_status




@app.get("/items")
def read_item(item_id: int, q: Union[str, None] = None):

    # api-endpoint
    URL = "http://172.17.0.3:8000/items"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'item_id':item_id, 'q':q}
  
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params=PARAMS)
  
    # extracting data in json format
    data = r.json()
    # print(data)
    return data