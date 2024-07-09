# Checks the mode user wishes to use.
def mode(graphType, routes, mode = -1):
    if graphType == 1:
        while mode != 1 and mode != 2 and mode != 3:
            m1 = ["One-to-All", "All-to-All"]
            mode = int(input(f"\nPath Mode (1: {m1[routes-1]}, 2: Dijkstra, 3: Salesman): "))
    elif graphType == 2:
        while mode != 1 and mode != 2:
            mode = int(input("\nPath Mode (1: One-to-All, 2: Djikstra): "))
    return mode

# Checks the graph user wishes to use.
def graph(graph = -1):
    while graph < 1 or graph > 2:
        graph = int(input("\nSearch Type (1: Undirected, 2: Directed): "))
    return graph

# Checks the source node user wishes to use.
def sourceNode(n, mode, routes, sourceNode = -1):
    if mode == 1 and routes == 2:
        return 0
    while sourceNode >= n or sourceNode < 0:
        sourceNode = int(input(f"\nSource Node (0 - {n-1}): "))
    return sourceNode

# Checks the destination node user wishes to use.
def destNode(mode, n, sourceNode, destNode = -1):
    if mode == 2:
        while destNode >= n or destNode < 0 or destNode == sourceNode:
            destNode = int(input(f"\nDestination Node (0 - {n-1}): "))
        return destNode

# Checks the number of nodes user wishes to use.  
def node(n = -1):
    while n < 2:
        n = int(input("\nNumber of Nodes (2+): "))
    return n

# Checks the layout user wishes to use.
def layout(graphType, val=-1):
    if graphType == 2:
        max = 4
        func = ""
    else:
        max = 5
        func = ", 5: File Input"
    try: val = int(val)
    except: 
        val = -1
    while val < 0 or val > max:
        val = int(input(f"\nLayout (1: Random, 2: Circular, 3: Square, 4: Hex{func}): "))
    return val

# Checks the route type (Sparse or Connected that the user wishes to use).
def routeType(routes = -1):
    while routes != 1 and routes != 2:
        routes = int(input("\nRoute Type (1: Sparse, 2: Connected): "))
    return routes

def custom(custom=None):
    while custom != "Y" and custom != "N":
        custom = input("\nReal World Nodes (Y/N): ").upper()
    return True if custom == "Y" else False
        
    
def solver(type=-1):
    while type < 0 or type >2:
        type = int(input("\nCompare All (0) | Nearest Neighbour (1) | Cheapest Insertion (2): "))
    return type