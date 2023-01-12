pip install fastapi
pip install "uvicorn[standard]"
uvicorn main:app --reload

docker:
build img:
docker build -t supercheap-bl-fastapi:0.1 .
create docker and run:
docker run -p 5000:8000 --name SuperCheapBL-api-server supercheap-bl-fastapi:0.1

to stop docekr:
docker kill SuperCheapBL-api-server

example url for testing:
http://localhost:5000/items?item_id=5&q=somequery