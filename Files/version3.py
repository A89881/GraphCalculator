import tkinter as tk
from functools import partial
import matplotlib.pyplot as plt
import numpy as np
import math as m

class GraphingCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Graphing Calculator")

        # Create function label and entry box
        self.function_label = tk.Label(master, text="Function: ")
        self.function_label.grid(row=0, column=0)
        self.function_entry = tk.Entry(master)
        self.function_entry.grid(row=0, column=1)

        # Create x range label and entry boxes
        self.x_min_label = tk.Label(master, text="x_min: ")
        self.x_min_label.grid(row=1, column=0)
        self.x_min_entry = tk.Entry(master)
        self.x_min_entry.grid(row=1, column=1)
        self.x_max_label = tk.Label(master, text="x_max: ")
        self.x_max_label.grid(row=2, column=0)
        self.x_max_entry = tk.Entry(master)
        self.x_max_entry.grid(row=2, column=1)

        # Create button to plot function
        self.plot_button = tk.Button(master, text="Plot Function", command=self.plot_function)
        self.plot_button.grid(row=3, column=1)

    def plot_function(self):
        # Get function string from entry box
        function_str = self.function_entry.get()

        # Get x range from entry boxes
        x_min = float(self.x_min_entry.get())
        x_max = float(self.x_max_entry.get())
        x_range = (x_min, x_max)

        # Plot the function using plot_math_function
        plot_math_function(function_str, x_range)

def plot_math_function(function_str, x_range=(-10, 10), num_points=1000, clr="blue"):
    """
    Plots a mathematical function given as a string using Matplotlib.

    Parameters:
        function_str (str): The mathematical function to plot, in the form of a string.
        x_range (tuple): The range of x values to plot, in the form of a tuple (xmin, xmax).
        num_points (int): The number of points to plot.

    Returns:
        None
    """

    # Define the x values to plot
    x_vals = np.linspace(x_range[0], x_range[1], num_points)

    # Create a namespace for the math functions
    namespace = {'x': x_vals}
    namespace.update(m.__dict__)

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
    plt.title(function_str)
    plt.legend()

    # Show the plot
    plt.show()  

root = tk.Tk()
graphing_calculator = GraphingCalculator(root)
root.mainloop()