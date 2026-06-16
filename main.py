from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class PipelineNode(BaseModel):
    id: str

    class Config:
        extra = 'allow'


class PipelineEdge(BaseModel):
    source: str
    target: str

    class Config:
        extra = 'allow'


class Pipeline(BaseModel):
    nodes: list[PipelineNode] = []
    edges: list[PipelineEdge] = []


def is_dag(nodes: list[PipelineNode], edges: list[PipelineEdge]) -> bool:
    node_ids = {node.id for node in nodes}
    adjacency = {node_id: [] for node_id in node_ids}
    indegree = {node_id: 0 for node_id in node_ids}

    for edge in edges:
        if edge.source not in node_ids or edge.target not in node_ids:
            continue

        adjacency[edge.source].append(edge.target)
        indegree[edge.target] += 1

    queue = [node_id for node_id, degree in indegree.items() if degree == 0]
    visited_count = 0

    while queue:
        node_id = queue.pop(0)
        visited_count += 1

        for neighbor in adjacency[node_id]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return visited_count == len(node_ids)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://vector-shift-web.vercel.app/'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
def read_root():
    return {'Ping': 'Pong'}


 

@app.post('/pipelines/parse')
def parse_pipeline(pipeline: Pipeline):
    return {
        'num_nodes': len(pipeline.nodes),
        'num_edges': len(pipeline.edges),
        'is_dag': is_dag(pipeline.nodes, pipeline.edges),
    }
