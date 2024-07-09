from math import sqrt, ceil
import networkx as nx

def selectLayout(G, n, layout, seed):
    if layout == 1: pos = nx.spring_layout(G, seed=seed)
    elif layout == 2: pos = nx.circular_layout(G)
    elif layout == 3: pos = squaregridLayout(n)
    else: pos = hexgridLayout(n)
    print("")
    return pos

def hexgridLayout(n):
    side_length = ceil(sqrt(n))
    pos = {}
    index = 0
    for i in range(side_length * 2):
        for j in range(side_length):
            x = j * sqrt(3)
            y = i * 0.75
            if i % 2 != 0:
                x += sqrt(3) / 2
            if index < n:
                pos[index] = (x, y)
                index += 1
    return pos

def squaregridLayout(n):
    side_length = ceil(sqrt(n))
    pos = {}
    index = 0
    for i in range(side_length):
        for j in range(side_length):
            pos[index] = (j, -i)
            index += 1
    return pos