# app.py
from fastapi import FastAPI
import requests, json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Sony"}


@app.get("/health")
async def health():
    return "Healthy"


@app.get("/diag")
async def root():
    res = requests.get(url="https://www.travel-advisory.info/api")
    res_json = res.json()
    return res_json["api_status"]["reply"]


@app.get("/convert/{label}")
async def convert_convert_code(label: str):
    res = requests.get(url="https://www.travel-advisory.info/api")
    user_input = label
    print(f"user input is {user_input}")
    # print(res.json())
    res_json = res.json()

    for i in res_json["data"]:
        if user_input.upper() == res_json["data"][i]["iso_alpha2"]:
            # return res_json['data'][user_input.upper()]['name']
            return f"Country name is : {res_json['data'][user_input.upper()]['name']}"
    else:
        return f"Country Code {user_input} not found"
