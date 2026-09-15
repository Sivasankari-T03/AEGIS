import { useState } from "react";
import { solveProblem } from "./services/api";
import "./App.css";

export default function App() {
  const [problem, setProblem] = useState("");
  const [result, setResult] = useState(null);

async function solve(){

    const data = await solveProblem(problem);

    setResult(data);

}
  return (
    <div className="container">
      <h1>🛡️ AEGIS</h1>
      <p>Adaptive Expert System</p>

      <textarea
        rows="4"
        placeholder="Enter your problem..."
        value={problem}
        onChange={(e) => setProblem(e.target.value)}
      />

      <button onClick={solve}>Solve</button>

      {result && (
  <div className="card">
    <h2>{result.result.algorithm}</h2>

    <p><strong>Category:</strong> {result.result.category}</p>

    <p><strong>Input:</strong> {result.input}</p>

    {result.solution && (
      <>
        <p><strong>Shortest Path:</strong></p>
        <h3>{result.solution.shortest_path.join(" → ")}</h3>
      </>
    )}
  </div>
)}
    </div>
  );
}