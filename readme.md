# Pipeline DAG Validator API

A lightweight FastAPI backend that analyzes a directed graph pipeline structure and determines whether it forms a Directed Acyclic Graph (DAG). It also returns basic pipeline statistics such as number of nodes and edges.

---

## 🚀 Features

- Accepts pipeline data (nodes + edges) via REST API
- Validates whether the pipeline is a DAG
- Returns:
  - Number of nodes
  - Number of edges
  - DAG validity result
- CORS enabled for frontend integration (React supported)

---

## 🧠 Core Logic

The system uses **Kahn’s Algorithm (Topological Sorting)** to determine whether the graph contains a cycle:

- Builds adjacency list from edges
- Computes indegree of each node
- Processes nodes with zero indegree
- If all nodes are processed → graph is a DAG

---

## 📦 Tech Stack

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn (recommended for running server)

---

## 📁 Project Structure


app.py # Main FastAPI application
models # Pydantic models (Pipeline, Node, Edge)
logic # DAG validation algorithm (is_dag)


> (If your code is in a single file, everything resides in `app.py`.)

---

## 🧾 API Endpoints

### 🔹 Health Check

```http
GET /

Response:

{
  "Ping": "Pong"
}
🔹 Parse Pipeline
POST /pipelines/parse
Request Body
{
  "nodes": [
    { "id": "A" },
    { "id": "B" }
  ],
  "edges": [
    { "source": "A", "target": "B" }
  ]
}
Response
{
  "num_nodes": 2,
  "num_edges": 1,
  "is_dag": true
}
⚙️ Installation & Setup
1. Clone Repository
git clone <your-repo-url>
cd <your-repo-folder>
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install Dependencies
pip install fastapi uvicorn pydantic
4. Run Server
uvicorn app:app --reload

Server will run at:

http://127.0.0.1:8000
🌐 CORS Configuration

This API is configured to accept requests from:

http://localhost:3000

You can modify it here:

allow_origins=['http://localhost:3000']
📌 Use Case

This API is useful for:

Workflow / pipeline builders
Node-based editors (React Flow, etc.)
DAG validation systems
ETL pipeline verification
Graph structure analysis tools
🧪 Algorithm Complexity
Time Complexity: O(V + E)
Space Complexity: O(V + E)

Where:

V = number of nodes
E = number of edges
📄 License

MIT License (or specify your own)

👨‍💻 Author

Built with FastAPI for pipeline graph validation and analysis.


---
