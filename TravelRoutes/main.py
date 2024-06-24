import argparse
from HelperFunctions import check
from HelperFunctions.helper import arguments, clear_terminal
from PathDisplay.pathPlot import travelPaths

clear_terminal()

# Command Line Parsing Values
parser = argparse.ArgumentParser()

for arg in arguments:
    parser.add_argument(arg[0], arg[1])
args = parser.parse_args()

# Inputting Values using Error Checking
print("")
graphType = check.graph(args.graph)
n = check.node(args.n)

routes = check.routeType(args.routes) if graphType == 1 else 1
mode = check.mode(args.mode, graphType, routes)
solver = check.solver() if routes == 2 and graphType == 1 and mode == 3 else None

source = check.sourceNode(args.sourceNode, n, mode, routes)
dest = check.destNode(args.destNode, mode, n, source)

layout = check.layout(args.layout, graphType)
seed = check.seed(args.seed)

travelPaths(graphType, n, mode, source, dest, layout, seed, routes, solver, None, True)