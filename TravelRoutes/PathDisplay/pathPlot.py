import matplotlib.pyplot as plt
import networkx as nx
from PathAlgorithms.euclideanGraph import euclideanGraph, printSolution
from PathAlgorithms.heuristicSearch import Graph
from HelperFunctions.helper import obtainEdges, maxEdges, customLabels
from HelperFunctions.layouts import selectLayout

def travelledNodes(edgeList):
    travelled = []
    if  len(edgeList) == 0 or len(list(edgeList)[0]) == 3:
        return travelled
    for edge in edgeList[:-1:]:
        travelled.append(edge[1])
    return travelled

def travelPaths(graphType, n, mode, sourceNode, destNode, layout, seed, routes, solver = 0, file = None, opt = False, random=False):
    g = Graph(n)
    if layout != 5:
        # Initialising NetworkX Graph
        G = nx.DiGraph() if graphType == 2 else nx.Graph()

        #Adding Nodes to NetworkX Graph
        G.add_nodes_from([node for node in range(n)])
        if routes == 1:
            G.add_edges_from(obtainEdges(n))
        else:
            G.add_edges_from(maxEdges(n))
        pos = selectLayout(G, n, layout, seed)
        g.graph = nx.adjacency_matrix(G).toarray()
        if n <= 30:
            print("\nAdjacency Matrix with Euclidean Distances:\n")
            printSolution(g.graph,n)
    else: 
        G, pos, g.graph = euclideanGraph(n, layout, seed, routes, file, random)

    allEdges = G.edges(data=True)

    # Running Djikstra's Algorithm to Find Shortest Path to All Nodes
    if mode == 1 and routes == 1:
        edgeList, includedNodes = g.dijkstra(sourceNode)
        adjacentNodes = [node for node in G.nodes if node != sourceNode]

    # Running Optimising Algorithm to Find Shortest Path Between Two Nodes
    elif mode == 2:
        edgeList = g.dijkstra(sourceNode, destNode)
        
    # Running Optimising Algorithm to Find a Path To Travel All Nodes & Back
    elif mode == 3: 
        if solver == 1:
            edgeList = g.nearest_neighbour(sourceNode, routes, opt)
        elif solver == 2:
            edgeList = g.cheapest_insertion(sourceNode, opt)
        elif solver == 0:
            g.nearest_neighbour(sourceNode, routes, opt)
            g.cheapest_insertion(sourceNode, opt)
            edgeList = []
    
    edgeLabels = nx.get_edge_attributes(G, "weight")
    
    if layout == 5:
        # Annotate nodes with coordinates
        offset = 0.15  # Adjust the offset as needed 
        for node, (x, y) in pos.items():
            plt.text(x+0.2, y-0.15, f'({round(x,2)}, {round(y,2)})', fontsize=8, ha='center', va='center', color='blue')
        edgeLabels = {edge: "{:.2f}".format(weight) for edge, weight in nx.get_edge_attributes(G, 'weight').items()}

    if routes == 2 and mode == 1:
        includedEdges = includedNodes = []
        excludedEdges = edgeList = allEdges
        adjacentNodes = [node for node in G.nodes]
    else:
        # Selecting Edges that are in the Shortest Path(s)
        includedEdges = [(u,v) for (u, v, d) in allEdges if ((u,v) in edgeList or (v,u) in edgeList)]
        excludedEdges = [(u,v) for (u, v, d) in allEdges if ((u,v) not in edgeList or (v,u) not in edgeList)]
        adjacentNodes = [node for node in G.nodes if node != sourceNode and node != destNode]
    
    if n <= 50:
        plt.clf()
        # Drawing Edges
        nx.draw_networkx_edges(G, pos, edgelist=excludedEdges, width=1.5, edge_color="orange")
        nx.draw_networkx_edges(G, pos, edgelist=includedEdges, width=2, edge_color="red")

        # Drawing Nodes
        if mode != 1:
            includedNodes = [node for node in travelledNodes(edgeList) if node is not sourceNode]
            excludedNodes = [node for node in adjacentNodes if node not in travelledNodes(edgeList)]
        else:
            excludedNodes = [node for node in G.nodes if node != sourceNode and node not in includedNodes]

        nx.draw_networkx_nodes(G, pos, nodelist=includedNodes, node_color="yellow", node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=[sourceNode], node_color="green", node_size=400)
        nx.draw_networkx_nodes(G, pos, nodelist=excludedNodes, node_size=400)

        if mode == 2:
            nx.draw_networkx_nodes(G, pos, nodelist=[destNode], node_color="red", node_size=400)

        # Node Labels
        custom, node_labels = customLabels(n)
        if custom == True:
            nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=15,font_family="tahoma")
        else:
            nx.draw_networkx_labels(G, pos, font_size=15, font_weight="bold", font_family="sans-serif")

        # Edge Weight Labels
        nx.draw_networkx_edge_labels(G, pos, edgeLabels)

        # Plotting Graph
        plt.gca().margins(0.06)
        plt.axis("on")
        plt.title("Travelling Salesman Problem")
        plt.tight_layout()

        fig = plt.gcf()
        fig.canvas.manager.set_window_title('Graph Mapper')

        plt.show()