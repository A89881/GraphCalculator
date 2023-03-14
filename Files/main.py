import matplotlib.pyplot as plt
import numpy as np
import math
import tkinter as tk

class GraphingCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Graphing Calculator")

        # Create function input label and entry box
        self.function_label = tk.Label(master, text="Enter a function (in terms of x e.g., x + 1 or x**2): ")
        self.function_label.pack()
        self.function_entry = tk.Entry(master)
        self.function_entry.pack()

        # Create x range input label and entry boxes
        self.x_min_label = tk.Label(master, text="X-Min: ")
        self.x_min_label.pack()
        self.x_min_entry = tk.Entry(master)
        self.x_min_entry.pack()

        self.x_max_label = tk.Label(master, text="X-Max: ")
        self.x_max_label.pack()
        self.x_max_entry = tk.Entry(master)
        self.x_max_entry.pack()

        # Create color input label and entry box
        self.color_label = tk.Label(master, text="Color: ")
        self.color_label.pack()
        self.color_entry = tk.Entry(master)
        self.color_entry.pack()

        # Create plot button
        self.plot_button = tk.Button(master, text="Plot", command=self.plot_function)
        self.plot_button.pack()

    def plot_function(self):
        # Get function string and x range from entry boxes
        function_str = self.function_entry.get()
        x_min = float(self.x_min_entry.get())
        x_max = float(self.x_max_entry.get())
        x_range = (x_min, x_max)
        clr = str(self.color_entry.get())

        # Define the x values to plot
        num_points = abs(int(x_range[0])) + abs(int(x_range[1]))
        print(num_points)
        x_vals = np.linspace(x_range[0], x_range[1], num_points)

        # Create a namespace for the math functions
        namespace = {'x': x_vals}
        namespace.update(math.__dict__)

        # Evaluate the function for each x value
        try:
            y_vals = eval(function_str, namespace)
        except:
            print("Invalid function.")
            return

        # Create the plot
        plt.plot(x_vals, y_vals, label=function_str, color=clr)

        # Add labels and title
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.legend()

        # Show the plot
        plt.show()

root = tk.Tk()
graphing_calculator = GraphingCalculator(root)
root.mainloop()