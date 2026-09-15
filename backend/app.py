from fastapi import FastAPI
from classifier import classify_problem
from algorithms.bfs import bfs

app = FastAPI(title="AEGIS")

@app.get("/")
def home():
    return {
        "project": "AEGIS",
        "message": "Adaptive Expert System is running!"
    }

@app.get("/classify")
def classify(problem: str):
    return {
        "input": problem,
        "result": classify_problem(problem)
    }

@app.get("/bfs")
def shortest_path(start: str, goal: str):
    path = bfs(start, goal)

    return {
        "algorithm": "Breadth First Search",
        "start": start,
        "goal": goal,
        "shortest_path": path
    }