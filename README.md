# TSP Solver
The TSP Solver is an application which uses graph-search algorithms to investigate and find estimations to the Travelling Salesman Problem (TSP), which involves traversing edges to reach from one node to another.

The file structure for this project is explained below.

## Requirements
- To install the libraries and packages used in this project.

```pip install -r requirements.txt```

## TSP Solver
> The primary file that should be run to see the program in action.
- Uses the ```tkinter```library to create an applet through which one can change their settings and continuously generate graphs without need to rerun the code multiple times.

## Main
- An alternative to the TSP Solver, which requires user values to be inputted into the terminal.

## Path Algorithms
All files contain the backend/logical program that calculates and determines solutions.

### Euclidean Graph
- Creates a connected graph using a fixed layout template or calls ```visualization.py``` and uses file input values.
- Prints a matrix of Euclidean distances.

### Heuristic Search
Contains the logic code for:
- Dijkstra's Greedy Algorithm: To find the shortest paths from one node to another.
- Destination Mapping: The shortest individual paths from one node to all nodes.
- The Travelling Salesman Algorithm using the following heuristics:
    - Nearest Neighbour: Chooses the closest unvisited neighbouring node at every subtour to build a path. Most optimal with few nodes and has a low runtime.
    - Cheapest Insertion: Inserts nodes within existing ones to minimise the net travel cost. Highly optimal, but has a high runtime.

### Optimisation
- Contains the logic code for 2-opt and 3-opt tour improvement algorithms, which can be applied on any of the TSP algorithms.
- Uses the ```tqdm``` library to generate progress bars.

## Path Display
### Path Print
Contains functions which print out the path for:
- Dijkstra's Algorithm, Destination Mapping & the TSP.
- Prints the optimised paths and runtime.

### Path Plot
- Implements ```euclideanGraph```, ```heuristicSearch``` and ```HelperFunctions``` along with ```matplotlib``` and ```networkx``` to to construct a graph.
- Considers directed and undirected graphs.
- It is called by ```TSP Solver.py``` and ```main.py```.

## HelperFunctions
### Helper
Contains functions used throughout the project:
- _obtainEdges_ provides a randomised list of edges.
- _arguments_ provides the command line arguments.
- _shortestPathLength_ provides an integer shortest length between two nodes.
- _shortestPath_ provides the edges travelled along this path, in the form of a list of tuples.
- _clearTerminal_ removes any leftover code statements, making it clearer, especially when rerunning TSP Solver multiple times.
- _customLabels_ to rename nodes on the graph. Set the variable ```custom``` to True or False accordingly.

### Check
Error checks different inputs:
- The Number of Edges: Ensures a minimum of 2.
- The Source Node: Must be >= 0 or =< n -1.
- The Destination Node: Must not be equal to the source node.
- The Graph: Must be either undirected (1) or directed (2)
- Mode Check: Checks the mode is either 1 or 2.
- Layout Check: Ensures the layout is between 1 - 4.

### Layouts
Contains the code for 5 layouts, which arrange the nodes neatly:
- Random (with seed)
- Circular
- Square
- Hexagonal
- File Entry (Manual File based on user input).

## DataSample
### Visualization
- Used to read edges from files to create Euclidean graphs.

### Datasets
- Contains datasets (both custom and synthetic benchmark ones) which are used by ```visualization.py```.
    - C1k.1 and E1k.1 are synthetic datasets from:
    http://archive.dimacs.rutgers.edu/Challenges/TSP/results.html#Fast%20Tour%20Construction.
    - Test contains arbitary data points which I utilised for testing purposes.
    - Mumbai contains the actual geographical coordinates of locations in the city of Mumbai, India.
- Each dataset has 3 rows which contain its name, additional comments and the number of nodes.
- The remaining _n_ rows hold data the the format: index  x  y