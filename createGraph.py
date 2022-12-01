from bfs import bfs
from Node import Node
import random
import string


def create_graph_and_run_bfs(graphname, nodes, edges):
    adjList = dict()
    # create nodes, each having a unique name
    while len(adjList) < nodes:
        name = "".join(
            random.choices(string.ascii_lowercase, k=4)
        )  # edges will be named 'iefj' 'eooe' 'pppp' etc.
        newNode = Node(name, None, float("inf"), "White")
        adjList[newNode] = set()
    # create directed edges
    for i in range(edges):
        edge1 = random.choice(list(adjList.keys()))
        edge2 = random.choice(list(adjList.keys()))
        adjList[edge1].add(edge2)
    # pick a random source, and a random destination
    source = random.choice(list(adjList.keys()))
    destination = random.choice(list(adjList.keys()))
    # run BFS..
    bfs(graphname, adjList=adjList, s=source, t=destination)
