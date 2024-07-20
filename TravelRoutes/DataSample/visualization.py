import numpy as np 

prefix = "TravelRoutes/DataSample/Datasets/"
filenames = [f"{prefix}C1k.1", f"{prefix}E1k.1", f"{prefix}Test", f"{prefix}Mumbai"]

def visualize(n, file, random):
    filecode = file if file != None else 0
    while filecode > 4 or filecode < 1:
        filecode = int(input("\nEnter File (1: C1k.1, 2: E1k.1, 3: Test, 4: Mumbai): "))
    filename = filenames[filecode - 1]
    data = np.loadtxt(filename, skiprows =3)
    indices = np.random.choice(data.shape[0], size=n, replace=False) if random else np.arange(n)
    data = data[indices]
    x, y = list(data[:, 1]), list(data[:, 2])

    return [[x[i], y[i]] for i in range(n)]