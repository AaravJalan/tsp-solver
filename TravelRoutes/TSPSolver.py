import tkinter as tk
from tkinter import ttk, messagebox
from HelperFunctions.helper import clearTerminal
from PathDisplay.pathPlot import travelPaths


class TSPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TSP Solver")

        self.createWidgets()

    def createWidgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Graph Type
        ttk.Label(frame, text="Graph Type:").grid(row=0, column=0, sticky=tk.W)
        self.graph_var = tk.StringVar()
        graph_options = ["1: Undirected", "2: Directed"]
        self.graph_combobox = ttk.Combobox(frame, textvariable=self.graph_var, values=graph_options, state="readonly")
        self.graph_combobox.grid(row=0, column=1, sticky=tk.E)
        self.graph_combobox.current(0)

        # Number of Nodes
        ttk.Label(frame, text="Number of Nodes:").grid(row=1, column=0, sticky=tk.W)
        self.nodes_var = tk.IntVar(value=10)
        self.nodes_spinbox = ttk.Spinbox(frame, from_=2, to=10000, textvariable=self.nodes_var, command=self.updateSourceSpinbox)
        self.nodes_spinbox.grid(row=1, column=1, sticky=tk.E)

        # Routes
        ttk.Label(frame, text="Routes:").grid(row=2, column=0, sticky=tk.W)
        self.routes_var = tk.StringVar()
        routes_options = ["1: Sparse", "2: Connected"]
        self.routes_combobox = ttk.Combobox(frame, textvariable=self.routes_var, values=routes_options, state="readonly")
        self.routes_combobox.grid(row=2, column=1, sticky=tk.E)
        self.routes_combobox.current(1)

        # Mode
        ttk.Label(frame, text="Mode:").grid(row=3, column=0, sticky=tk.W)
        self.mode_var = tk.StringVar()
        mode_options = ["1: One-to-All", "2: Dijkstra", "3: Salesman"]
        self.mode_combobox = ttk.Combobox(frame, textvariable=self.mode_var, values=mode_options, state="readonly")
        self.mode_combobox.grid(row=3, column=1, sticky=tk.E)
        self.mode_combobox.current(2)

        # Source Node
        ttk.Label(frame, text="Source Node:").grid(row=4, column=0, sticky=tk.W)
        self.source_var = tk.IntVar(value=0)
        self.source_spinbox = ttk.Spinbox(frame, from_=0, to=self.nodes_var.get()-1, textvariable=self.source_var)
        self.source_spinbox.grid(row=4, column=1, sticky=tk.E)

        # Destination Node
        self.dest_label = ttk.Label(frame, text="Destination Node:")
        self.dest_var = tk.IntVar(value=1)
        self.dest_spinbox = ttk.Spinbox(frame, from_=0, to=self.nodes_var.get()-1, textvariable=self.dest_var)

        # Layout
        ttk.Label(frame, text="Layout:").grid(row=6, column=0, sticky=tk.W)
        self.layout_var = tk.StringVar()
        layout_options = ["1: Random", "2: Circular", "3: Square", "4: Hex", "5: File Input"]
        self.layout_combobox = ttk.Combobox(frame, textvariable=self.layout_var, values=layout_options, state="readonly")
        self.layout_combobox.grid(row=6, column=1, sticky=tk.E)
        self.layout_combobox.current(3)

        # File Option
        self.file_label = ttk.Label(frame, text="File:")
        self.file_var = tk.StringVar()
        file_options = ["1: C1k.1", "2: E1k.1", "3: Test", "4: Mumbai"]
        self.file_combobox = ttk.Combobox(frame, values=file_options, textvariable=self.file_var, state="readonly")

        # Random Checkbox
        self.rand_checkbutton = ttk.Checkbutton(frame)
        self.rand_label = ttk.Label(frame, text="Randomise")
        self.rand_var = tk.BooleanVar(value=False)
        self.rand_checkbutton.config(variable=self.rand_var)

        # Solver
        self.solver_label = ttk.Label(frame, text="Solver:")
        self.solver_var = tk.StringVar()
        solver_options = ["0: Compare All", "1: Nearest Neighbour", "2: Cheapest Insertion"]
        self.solver_combobox = ttk.Combobox(frame, textvariable=self.solver_var, values=solver_options, state="readonly")
        self.solver_label.grid(row=9, column=0, sticky=tk.W)
        self.solver_combobox.grid(row=9, column=1, sticky=tk.E)
        self.solver_combobox.current(1)

        # OPT Checkbox
        self.opt_checkbutton = ttk.Checkbutton(frame)
        self.opt_label = ttk.Label(frame, text="Optimise")
        self.opt_var = tk.BooleanVar(value=False)
        self.opt_checkbutton.config(variable=self.opt_var)
        self.opt_label.grid(row=10, column=0, sticky=tk.W)
        self.opt_checkbutton.grid(row=10, column=1, columnspan=2, sticky=tk.W)

        # Seed
        ttk.Label(frame, text="Seed:").grid(row=11, column=0, sticky=tk.W)
        self.seed_var = tk.IntVar(value=0)
        self.seed_spinbox = ttk.Spinbox(frame, from_=0, to=1000, textvariable=self.seed_var)
        self.seed_spinbox.grid(row=11, column=1, sticky=tk.E)

        # Start Button
        tk.Button(frame, text="Start", command=self.startAlgorithm, bg='green', activebackground='blue').grid(row=12, column=0, columnspan=2, sticky=(tk.W, tk.E))
    
        self.graph_combobox.bind("<<ComboboxSelected>>", self.updateGraphVisibility)
        self.mode_combobox.bind("<<ComboboxSelected>>", self.updateModeVisibility)
        self.layout_combobox.bind("<<ComboboxSelected>>", self.updateFileComboboxVisibility)
        
    def updateSourceSpinbox(self):
        self.source_spinbox.config(to=self.nodes_var.get()-1)

    def updateModeVisibility(self, event):
        if self.mode_var.get().startswith("2:"):
            self.dest_label.grid(row=5, column=0, sticky=tk.W)
            self.dest_spinbox.grid(row=5, column=1, sticky=tk.E)
        else:
            self.dest_label.grid_forget()
            self.dest_spinbox.grid_forget()

        if self.mode_var.get().startswith("3") and self.graph_var.get().startswith("1"):
            self.solver_label.grid(row=9, column=0, sticky=tk.W)
            self.solver_combobox.grid(row=9, column=1, sticky=tk.E)
            self.solver_combobox.current(1)
            self.opt_checkbutton.grid(row=10, column=1, columnspan=2, sticky=tk.W)
            self.opt_label.grid(row=10, column=0, columnspan=2, sticky=tk.W)
            
    def updateGraphVisibility(self, event):
        if self.graph_var.get().startswith("2:"):  # Directed
            self.mode_combobox.config(values=["1: One-to-All", "2: Dijkstra"])
            if self.mode_var.get().startswith("3:"):
                self.mode_combobox.current(0)  # Default to first option if invalid
                self.solver_label.grid_forget()
                self.solver_combobox.grid_forget()
                self.opt_checkbutton.grid_forget()
                self.opt_label.grid_forget()
        else:
            self.mode_combobox.config(values=["1: One-to-All", "2: Dijkstra", "3: Salesman"])
        
        if self.graph_var.get().startswith("2:"):  # Directed
            self.layout_combobox.config(values=["1: Random", "2: Circular", "3: Square", "4: Hex"])
            if self.layout_var.get().startswith("5:"):
                self.layout_combobox.current(0)  # Default to first option if invalid
        else:
            self.layout_combobox.config(values=["1: Random", "2: Circular", "3: Square", "4: Hex", "5: File Input"])
        
        self.updateFileComboboxVisibility(None)  # Ensure layout update reflects file visibility changes

    def updateFileComboboxVisibility(self, event):
        if self.layout_var.get().startswith("5:"):
            self.file_label.grid(row=7, column=0, sticky=tk.W)
            self.file_combobox.grid(row=7, column=1, sticky=tk.E)
            self.file_combobox.current(2)
            self.rand_checkbutton.grid(row=8, column=1, columnspan=2, sticky=tk.W)
            self.rand_label.grid(row=8, column=0, columnspan=2, sticky=tk.W)
        else:
            self.file_label.grid_forget()
            self.file_combobox.grid_forget()
            self.rand_checkbutton.grid_forget()
            self.rand_label.grid_forget()

    def startAlgorithm(self):
        clearTerminal()
        try:
            graphType = int(self.graph_var.get()[0])
            n = self.nodes_var.get()
            routes = int(self.routes_var.get()[0]) if graphType == 1 else 1
            mode = int(self.mode_var.get()[0])
            opt = None
            if routes == 2 and graphType == 1:
                solver = int(self.solver_var.get()[0])
                if mode == 3: opt = self.opt_var.get()
            else:
                solver = -1
            source = self.source_var.get()
            dest = self.dest_var.get() if mode == 2 else None
            layout = int(self.layout_var.get()[0])
            file = int(self.file_var.get()[0]) if layout == 5 else None
            random = self.rand_var.get() if layout == 5 else False
            seed = self.seed_var.get()

            travelPaths(graphType, n, mode, source, dest, layout, seed, routes, solver, file, opt, random)

        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = TSPApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()