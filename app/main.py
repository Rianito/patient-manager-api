from fastapi import FastAPI
from routers import patient
from pymongo import MongoClient
from dotenv import dotenv_values
from uvicorn import run

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["DB_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(patient)

@app.get("/")
def read_home():
    return "teste"

if __name__ == "__main__":
    run("main:app", port=5000, log_level="info")