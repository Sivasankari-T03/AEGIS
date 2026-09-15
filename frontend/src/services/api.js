const API = "http://127.0.0.1:8000";

export async function solveProblem(problem){

    const classify = await fetch(
        `${API}/classify?problem=${encodeURIComponent(problem)}`
    );

    const result = await classify.json();

    if(result.result.algorithm==="BFS"){

        const bfs = await fetch(`${API}/bfs?start=S&goal=G`);

        const bfsResult = await bfs.json();

        return {
            ...result,
            solution:bfsResult
        };
    }

    return result;
}