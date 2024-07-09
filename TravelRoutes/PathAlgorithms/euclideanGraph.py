import networkx as nx
import numpy as np
from DataSample.visualization import visualize
from HelperFunctions.layouts import selectLayout
from HelperFunctions.helper import customLabels
from random import randint
from prettytable import PrettyTable
from colorama import Fore, Style

def printSolution(matrix, n):
    custom, node_labels = customLabels(n)
    table = PrettyTable()
    if custom:
        header = [''] + [node_labels[i] for i in range(n)]
    else:
        header = [''] + [str(i) for i in range(n)]
    table.field_names = header
    table.padding_width = 2
    for i, row in enumerate(matrix):
        if custom:
            table.add_row([node_labels[i]] + list(row))
        else:
            table.add_row([str(i)] + list(row))
        
    print(Fore.BLUE, end="")
    print(table)
    print(Style.RESET_ALL)

def adjacencyMatrix(n, edges):
    matrix = [[0] * n for _ in range(n)]

    # Update matrix based on edges
    for edge in edges:
        u, v, t = edge
        matrix[u][v] = t['weight']
        matrix[v][u] = t['weight']

    return matrix

def obtainRealEdges(mapping, n, nodes, routes):
    count = 0
    edges = []
    for i in range(n):
        if n <= 12:
            rand = randint(2, 3)
        else:
            rand = n//3
        for j in range(i+1, n):
            node1, node2 = mapping[i], mapping[j]
            distance = np.linalg.norm(np.array(nodes[node1]) - np.array(nodes[node2]))
            if count % rand == 1:
                edges.append((i, j, {'weight' : distance}))
            count += 1
    return edges

def euclideanGraph(n, layout, seed, routes, file, random):
    if routes == 2:
        # Create a complete graph
        G = nx.complete_graph(n)

        # Add nodes with x and y coordinates
        nodes = {}

        if layout == 5: pos = visualize(n, file, random)
        else: pos = selectLayout(G, n, layout, seed)

        for i in range (n):
            nodes.update({i: pos[i]})

        # Relabel nodes with coordinates
        mapping = dict(enumerate(nodes.keys()))
        G = nx.relabel_nodes(G, mapping)

        # Calculate distances between nodes and set them as weights
        for node1, node2 in G.edges():
            original_node1, original_node2 = mapping[node1], mapping[node2]
            distance = np.linalg.norm(np.array(nodes[original_node1]) - np.array(nodes[original_node2]))
            G[node1][node2]['weight'] = distance

        # Create a layout based on distances
        pos = {node: np.array(nodes[node]) for node in G.nodes()}
        
        if n <= 19:
            # Get the adjacency matrix with distance values
            adj_matrix = nx.adjacency_matrix(G).toarray()
            np.set_printoptions(precision=2, suppress=True)
            print("\nAdjacency Matrix with Euclidean Distances:\n")
            adj_matrix = np.round(adj_matrix, 2)
            printSolution(adj_matrix, n)

        matrix = adjacencyMatrix(n, G.edges(data=True))
        return G, pos, matrix
    
    else:
        # G = nx.complete_graph(n)
        G = nx.Graph()

        # Add nodes with x and y coordinates
        nodes = {}

        if layout == 5: pos = visualize(n, file, random)
        else: pos = selectLayout(G, n, layout, seed)

        for i in range (n):
            nodes.update({i: pos[i]})

        # Relabel nodes with coordinates
        mapping = dict(enumerate(nodes.keys()))
        G = nx.relabel_nodes(G, mapping)

        # Adding edges to the graph
        G.add_edges_from(obtainRealEdges(mapping, n, nodes, routes))

        # Create a layout based on distances
        pos = {node: np.array(nodes[node]) for node in G.nodes()}
        matrix = adjacencyMatrix(n, G.edges(data=True))
        return G, pos, matrix