from algorithms.astar import astar

path, cost = astar("S", "G")

print("Optimal Path:", path)
print("Total Cost:", cost)