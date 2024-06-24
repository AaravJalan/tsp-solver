from tqdm import tqdm

def total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    return total_distance

def two_opt(path, graph):
    best_path = path
    improved = True
    with tqdm(total=len(path), desc="2-opt", unit="iteration") as pbar: 
        while improved:
            improved = False
            for i in range(1, len(best_path) - 2):
                for j in range(i + 1, len(best_path) - 1):
                    if j - i == 1: continue # Skip adjacent edges
                    new_path = best_path[:i] + best_path[i:j][::-1] + best_path[j:]
                    if total_distance(new_path, graph) < total_distance(best_path, graph):
                        best_path = new_path
                        improved = True
                pbar.update(1)
    return best_path

def three_opt(path, graph):
    best_path = path
    improved = True
    with tqdm(total=len(path), desc="3-opt", unit="iteration") as pbar:
        while improved:
            improved = False
            n = len(best_path)
            for i in range(1, n - 3):
                for j in range(i + 1, n - 2):
                    for k in range(j + 1, n - 1):
                        new_path = reverse_three_segment(best_path, i, j, k)
                        if total_distance(new_path, graph) < total_distance(best_path, graph):
                            best_path = new_path
                            improved = True
                    pbar.update(1)
    return best_path

def reverse_three_segment(path, i, j, k):
    new_path = path[:i] + path[i:j+1][::-1] + path[j+1:k+1][::-1] + path[k+1:]
    return new_path