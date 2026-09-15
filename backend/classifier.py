def classify_problem(text: str):
    text = text.lower()

    if "shortest path" in text or "maze" in text:
        return {
            "category": "Search",
            "algorithm": "BFS"
        }

    elif "sudoku" in text:
        return {
            "category": "CSP",
            "algorithm": "Backtracking"
        }

    elif "diagnosis" in text or "rule" in text:
        return {
            "category": "Logic",
            "algorithm": "Forward Chaining"
        }

    return {
        "category": "Unknown",
        "algorithm": "Manual Selection"
    }