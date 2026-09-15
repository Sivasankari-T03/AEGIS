from fastapi import FastAPI
from classifier import classify_problem
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar

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
@app.get("/dfs")
def depth_first(start: str, goal: str):

    path = dfs(start, goal)

    return {
        "algorithm": "Depth First Search",
        "start": start,
        "goal": goal,
        "path": path
    }
@app.get("/astar")
def optimal_route(start: str, goal: str):

    path, cost = astar(start, goal)

    return {
        "algorithm": "A* Search",
        "start": start,
        "goal": goal,
        "optimal_path": path,
        "total_cost": cost
    }