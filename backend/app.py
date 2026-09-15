from fastapi import FastAPI
from classifier import classify_problem

app = FastAPI(title="AEGIS")

@app.get("/")
def home():
    return {
        "project": "AEGIS",
        "status": "Running"
    }

@app.get("/classify")
def classify(problem: str):
    result = classify_problem(problem)
    return {
        "input": problem,
        "result": result
    }