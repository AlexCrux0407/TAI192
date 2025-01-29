from fastapi import FastAPI

app = FastAPI()

#endpoint home
@app.get("/")

def home():
    return {"hello": "world FastAPI"}