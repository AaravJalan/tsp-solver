from tqdm import tqdm

## Finds the total distance travelled along a path in a given graph.
def totalDistance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    return total_distance

## Optimisation problems attempt to find the path with the shortest travel cost.
## 2-opt optimization algorithm for path improvement.
def twoOpt(path, graph):
    bestPath = path
    improved = True
    ## Shows a progress bar for the 3-opt optimization.
    with tqdm(total=len(path), desc="2-opt", unit="iteration") as pbar: 
        ## Continue until no improvement is made.
        while improved:
            improved = False
            ## Iterate through all possible pairs of edges.
            for i in range(1, len(bestPath) - 2):
                for j in range(i + 1, len(bestPath) - 1):
                    if j - i == 1: continue # Skip adjacent edges
                    new_path = bestPath[:i] + bestPath[i:j][::-1] + bestPath[j:]
                    ## If the travel cost is less, the path is more optimised and better.
                    if totalDistance(new_path, graph) < totalDistance(bestPath, graph):
                        bestPath = new_path
                        improved = True
                pbar.update(1)
    return bestPath

## 3-opt optimization algorithm for path improvement.
def threeOpt(path, graph):
    bestPath = path
    improved = True
    ## Shows a progress bar for the 3-opt optimization.
    with tqdm(total=len(path), desc="3-opt", unit="iteration") as pbar:
        ## Continue until no improvement is made.
        while improved:
            improved = False
            n = len(bestPath)
            ## Iterate through all possible pairs of edges.
            for i in range(1, n - 3):
                for j in range(i + 1, n - 2):
                    for k in range(j + 1, n - 1):
                        new_path = reverseThreeSegment(bestPath, i, j, k)
                        ## If the travel cost is less, the path is more optimised and better.
                        if totalDistance(new_path, graph) < totalDistance(bestPath, graph):
                            bestPath = new_path
                            improved = True
                    pbar.update(1)
    return bestPath

## Reverses the three segments of a path from i to j, j to k, and k to the end.
def reverseThreeSegment(path, i, j, k):
    newPath = path[:i] + path[i:j+1][::-1] + path[j+1:k+1][::-1] + path[k+1:]
    return newPath