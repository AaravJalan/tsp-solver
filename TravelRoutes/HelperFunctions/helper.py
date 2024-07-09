from random import randint
import networkx as nx
import os

def obtainEdges(n):
    count = 0
    edges = []
    for i in range(n):
        if n <= 12:
            rand = randint(2, 3)
        else:
            rand = n//3
        for j in range(i+1, n):
            if count % rand == 1:
                weight = randint(1,14)
                edges.append((i, j, {'weight' : weight}))
            count += 1
    return edges

def maxEdges(n):
    edges = []
    for i in range(n):
        for j in range(n):
            if i != j:
                weight = randint(1,14)
                edges.append((i, j, {'weight' : weight}))
    return edges

def shortestPathLength(G, src, dest):
    try:
        return nx.shortest_path_length(G, source=src, target=dest, weight='weight')
    except nx.NetworkXNoPath:
        return None, float('inf')

def shortestPath(G, src, dest):
    edges = []
    try:
        shortestPath = nx.shortest_path(G, source=src, target=dest, weight='weight')
        for i in range(len(shortestPath)-1):
            edges.append((shortestPath[i],shortestPath[i+1]))
        return edges
    except nx.NetworkXNoPath:
            return None, float('inf')

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def customLabels(n=-1):
    custom = False
    nodes_list = ["Prabhadevi", "Mahalaxmi", "Andheri", "Bandra", "Juhu","Churchgate","Sion", "Matunga", "Santacruz"]
    if n == -1: n = len(nodes_list)
    node_labels = {i: nodes_list[i] for i in range(min(n, len(nodes_list)))}
    return custom, node_labels