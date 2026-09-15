from fastapi import FastAPI
from classifier import classify_problem
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar
from algorithms.backtracking import solve

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
@app.get("/sudoku")
def sudoku_demo():

    board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]

    solve(board)

    return {
        "algorithm":"Backtracking",
        "solution":board
    }