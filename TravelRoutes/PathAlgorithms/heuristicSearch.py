import sys
from colorama import Fore, Style
from PathDisplay.pathPrint import printSolution, printPath, displayPath
from tqdm import tqdm
import time

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for c in range(vertices)] for r in range(vertices)]
 
    # Finds the vertex with the minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = sys.maxsize
 
        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
                
        try: return min_index
        except: return -1
 
    # Function that implements Dijkstra's single source shortest path algorithm.
    def dijkstra(self, src, target=None):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        parent = [-1] * self.V
 
        for _ in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
 
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
                    parent[y] = x

        # Returns the shortest path from the source to all nodes.
        if target is None:
            paths = []
            for node in range(self.V):
                path = [node]
                while node != src:
                    path.append(parent[node])
                    node = parent[node]
                paths.append(path[::-1])
            included = printSolution(dist, paths, self.V, self.graph)
            return [(parent[i],i) for i in range(0, self.V)], included
        
        # Returns the shortest path from the source to the target.
        else:
            node = target
            edges = []
            path = [node]
            while node != src:
                edges.append((parent[node], node))
                path.append(parent[node])
                node = parent[node]
            print(Fore.GREEN + f"\nThe Shortest Distance: {round(dist[target],2)}\n")
            print(Fore.BLUE + f"The Path Taken: {displayPath(path[::-1])}") 
            print(Style.RESET_ALL)
            return edges[::-1]
    
    # Helper Function to Find Nearest Neighbouring Nodes
    def iterate(self, tick):
        closest = sys.maxsize
        nearest = -1
        tick = tick
        adjacent = self.graph[self.src]
        while nearest == -1:
            for v in range(self.V):
                if self.visited[v] == tick and 0 < adjacent[v] < closest:
                    closest = adjacent[v]
                    nearest = v
            tick += 1
        self.distanceTravelled += closest
        if (self.src, nearest) not in self.visitedEdges:
            self.visitedEdges.append((self.src, nearest))
        self.path.append(nearest)    
        self.visited[nearest] += 1
        self.src = nearest

    # Function to Find Paths to All Nodes and Back
    def nearestNeighbour(self, src, routes, opt):
        source = self.src = src
        self.visited = [0] * self.V
        self.visitedEdges = []
        self.visited[src] = 1
        self.distanceTravelled = 0
        self.path = [src]
        self.routes = routes
        print("")
        start_time = time.time()
        with tqdm(total=self.V, desc="Nearest Neighbour Algorithm", unit="node") as pbar:
            while min(self.visited) == 0:
                self.iterate(0)
                pbar.update(1)
        path = self.path
        end_time = time.time()
        print(f"NN took {end_time - start_time:.4f} seconds")
        if self.routes == 1:
            self.path = []
            while self.src != source:
                self.iterate(1)
            self.returnPath = self.path
            self.returnPath.insert(0, path[-1])
            printPath(path, self.graph, opt, self.routes, self.returnPath)
            
        else:
            self.visitedEdges.append((path[-1],source))
            self.distanceTravelled += self.graph[path[-1]][source]
            path.append(source)
            printPath(path, self.graph, opt)
    
        return self.visitedEdges

    def cheapestInsertion(self, source, opt):
        n = len(self.graph)
        unvisited = set(range(n))
        unvisited.remove(source)
        self.distanceTravelled = 0

        nearest_node = min(unvisited, key=lambda node: self.graph[source][node])
        path = [source, nearest_node]
        unvisited.remove(nearest_node)
        print("")
        start_time = time.time()
        with tqdm(total=self.V, desc="Cheapest Insertion Algorithm", unit="node") as pbar:
            while unvisited:
                # Find the nearest unvisited node to any node in the current path
                min_distance = float('inf')
                best_node = None
                best_position = None

                # Find the best position to insert the nearest node into the path
                for node in unvisited:
                    for i in range(1, len(path)):
                        prev_node = path[i - 1]
                        next_node = path[i]
                        increase = (self.graph[prev_node][node] +
                                    self.graph[node][next_node] -
                                    self.graph[prev_node][next_node])
                        
                        if increase < min_distance:
                            min_distance = increase
                            best_node = node
                            best_position = i
                pbar.update(1)

                # Insert the nearest node at the best position
                path.insert(best_position, best_node)
                unvisited.remove(best_node)
        end_time = time.time()
        print(f"CI took {end_time - start_time:.4f} seconds")
        path.append(source)
        printPath(path, self.graph, opt)
        self.visitedEdges = []
        for i in range(n):
            self.visitedEdges.append((path[i], path[i+1]))

        return self.visitedEdges