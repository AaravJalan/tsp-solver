# TSP Solver
The TSP Solver is an algorithm used to investigate and find estimations to the travelling salesman problem, which involves travelling edges to reach from one node to another.

The file structure for this project is explained below.

## Requirements
- To install the libraries and packages used in this project.

```pip install -r requirements.txt```

## TSP Solver
> The primary file that should be run to see the program in action.
- Uses the ```tkinter```library to create an applet through which one can change their settings and continuously generate graphs without need to rerun the code multiple times.

## Main
- An alternative to the TSP Solver, which requires user values to be inputted into the terminal.
- The advantage of this file is access to command line arguments. An example is below:
 ```python main.py -n 9 -g 2 -l 2 -m 1 -s 1 -d 7 -r 2```

## Path Algorithms
All files contain the backend/logical program that calculates and determines solutions.

### Euclidean Graph
- Creates a connected graph using a fixed layout template or calls ```visualization.py``` and uses file input values.
- Prints a matrix of Euclidean distances.

### Heuristic Search
Contains the logic code for:
- Dijkstra's Greedy Algorithm.
- Destination Mapping between 2 Nodes.
- The Travelling Salesman Algorithm using the:
    - Nearest Neighbour Heuristic
    - Cheapest Insertion Heuristic

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
- _clear\_terminal_ removes any leftover code statements, making it clearer, especially when rerunning TSP Solver multiple times.
- _customLabels_ to rename nodes on the graph. Set the variable ```custom``` to True or False accordingly.

### Check
Error checks different inputs:
- The Number of Edges: ensures a minimum of 2.
- The Source Node: must be >= 0 or =< n -1.
- The Destination Node: must not be equal to the source node.
- The Graph: Must be either undirected (1) or directed (2)
- Mode Check: checks the mode is either 1 or 2.
- Seed Check: It must be an integer >= 0, else defaults it to 0.
- Layout Check: Ensures the layout is between 1 - 4.

### Layouts
Contains the code for 5 layouts, which arrange the nodes neatly:
- Random (with seed)
- Circular
- Square
- Hexagonal
- Manual Layout based on user input.

## DataSample
### Visualization
- Used to read edges from files to create Euclidean graphs.

### Datasets
- Contains datasets (both custom and synthetic benchmark ones) which are used by ```visualization.py```.