from HelperFunctions import check
from HelperFunctions.helper import clearTerminal
from PathDisplay.pathPlot import travelPaths

clearTerminal()

# Inputting Values using Error Checking
graphType = check.graph()
n = check.node()

routes = check.routeType() if graphType == 1 else 1
mode = check.mode(graphType, routes)
solver = check.solver() if routes == 2 and graphType == 1 and mode == 3 else None

source = check.sourceNode(n, mode, routes)
dest = check.destNode(mode, n, source)

layout = check.layout(graphType)
seed = 0

travelPaths(graphType, n, mode, source, dest, layout, seed, routes, solver, None, True)