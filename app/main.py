from fastapi import FastAPI,Request
import pickle
import numpy as np
from app.code import predict
import os

model = pickle.load(open(os.getcwd()+r'/model/model.pkl','rb'))

app = FastAPI()

@app.post("/api/type")
async def typename(data : Request):
    json = await data.json()
    imgStr = json["img"]
    animal = predict(model,imgStr)
    return {"Type" : animal}