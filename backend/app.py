from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "AEGIS",
        "message": "Adaptive Expert System is running!"
    }