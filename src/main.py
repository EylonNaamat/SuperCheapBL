from typing import Union
import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def read_item(item_id: int, q: Union[str, None] = None):
    print('1')

    # api-endpoint
    URL = "http://172.17.0.3:8000/items"
    print('2')

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'item_id':item_id, 'q':q}
  
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params=PARAMS)
    print('3')
  
    # extracting data in json format
    data = r.json()
    print('4')
    # print(data)
    return data