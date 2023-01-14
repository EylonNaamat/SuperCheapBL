FROM python:3.9-slim
COPY  ./src /SuperCheapBL/src
COPY ./requirements.txt /SuperCheapBL
COPY ./signup.py /SuperCheapBL

WORKDIR /SuperCheapBL

RUN pip install fastapi uvicorn requests
RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "uvicorn", "src.main:app", "--host=0.0.0.0", "--reload" ]