# Checks the mode user wishes to use.
def mode(mode, graphType, routes):
    try: mode = int(mode)
    except: 
        mode = -1
    if graphType == 1:
        while mode != 1 and mode != 2 and mode != 3:
            m1 = ["One-to-All", "All-to-All"]
            mode = int(input(f"\nPath Mode (1: {m1[routes-1]}, 2: Dijkstra, 3: Salesman): "))
    elif graphType == 2:
        while mode != 1 and mode != 2:
            mode = int(input("\nPath Mode (1: One-to-All, 2: Djikstra): "))
    return mode

# Checks the graph user wishes to use.
def graph(graph):
    try: graph = int(graph)
    except: graph = -1
    while graph < 1 or graph > 2:
        graph = int(input("\nSearch Type (1: Undirected, 2: Directed): "))
    return graph

# Checks the source node user wishes to use.
def sourceNode(sourceNode, n, mode, routes):
    if mode == 1 and routes == 2:
        return 0
    try: sourceNode = int(sourceNode)
    except: sourceNode = -1
    while sourceNode >= n or sourceNode < 0:
        sourceNode = int(input(f"\nSource Node (0 - {n-1}): "))
    return sourceNode

# Checks the destination node user wishes to use.
def destNode(destNode, mode, n, sourceNode):
    if mode == 2:
        try: destNode = int(destNode)
        except: destNode = -1
        while destNode >= n or destNode < 0 or destNode == sourceNode:
            destNode = int(input(f"\nDestination Node (0 - {n-1}): "))
        return destNode

# Checks the number of nodes user wishes to use.  
def node(n):
    try: n = int(n)
    except: n = -1
    while n < 2:
        n = int(input("\nNumber of Nodes (2+): "))
    return n

# Checks if seed is valid else sets a default value.
def seed(seed):
    try: return int(seed)
    except: return 0

# Checks the layout user wishes to use.
def layout(val, graphType):
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
def routeType(routes):
    while routes != 1 and routes != 2:
        routes = int(input("\nRoute Type (1: Sparse, 2: Connected): "))
    return routes

def solver(type=-1):
    while type < 0 or type >2:
        type = int(input("\nCompare All (0) | Nearest Neighbour (1) | Cheapest Insertion (2): "))
    return type