from prettytable import PrettyTable
from colorama import Fore, Style
import time, sys
from HelperFunctions.helper import customLabels
from PathAlgorithms.optimisation import twoOpt, threeOpt, totalDistance

custom, node_labels = customLabels()

def displayPath(path):
    if len(path) == 1 or min(path) < 0:
        return "---"
    if custom:
        return ' → '.join([node_labels[node] for node in path])
    return ' → '.join(map(str, path))

def printSolution(dist, paths, V, graph):
    table = PrettyTable(align="l")
    table.field_names = ["Vertex", "Distance", "Path"]

    # If the distance is infinite (highest possible integer), then the path doesn't exist.
    dist = [node if node != sys.maxsize else "Not Possible" for node in dist]

    included = []
    for node in range(V):
        if dist[node] != "Not Possible":
            included.append(node)
            path = paths[node]
            statement = printPath(path, graph)
            table.add_row([node, dist[node], statement])
        
    print(Fore.BLUE, table, "\n", Style.RESET_ALL)
    return included

def printPath(path, graph, opt=None, routes=0, returnPath=[]):
    unit = "km" if custom else ""
    if len(path) <= 50:
        print(Fore.BLUE + "\nPath: ", displayPath(path))
        if routes == 1:
            print(Fore.RED + "\nReturn Path: ", displayPath(returnPath))
    print(Fore.GREEN + f"\nDistance Travelled: {round(totalDistance(path, graph),2)} {unit}") 
    print(Fore.YELLOW + f"\nNodes: {len(path)} \n" + Style.RESET_ALL)
    
    if opt:
        # Apply 2-opt optimization to the initial path
        start_time = time.time()
        optimized_path = twoOpt(path, graph)
        end_time = time.time()
        print(f"2-opt optimization took {end_time - start_time:.4f} seconds")
        if len(path) <= 50:
            print(Fore.CYAN + "\n2-opt Optimized Path: ", displayPath(optimized_path), "\n")
        optimized_distance = totalDistance(optimized_path, graph)
        print(Fore.MAGENTA + f"2-opt Optimization Distance: {round(optimized_distance, 2)}  {unit}\n" + Style.RESET_ALL)
    
        # Apply 3-opt optimization to the 2-opt optimized path
        start_time = time.time()
        final_path = threeOpt(optimized_path, graph)
        end_time = time.time()
        print(f"3-opt optimization took {end_time - start_time:.4f} seconds")
        if len(path) <= 50:
            print(Fore.CYAN + "\n3-opt Optimized Path: ", displayPath(final_path), "\n")
        final_distance = totalDistance(final_path, graph)
        print(Fore.MAGENTA + f"3-opt Optimization Distance: {round(final_distance, 2)}  {unit}\n" + Style.RESET_ALL)