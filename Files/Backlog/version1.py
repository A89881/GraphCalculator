import matplotlib.pyplot as plt
import numpy as np
import math as m
import tkinter as tk

class graph_function:
    def __init__(self, x_range=(-10, 10), num_points=1000, clr="blue"):
        self.x_range = x_range
        self.num_points = num_points
        self.clr = clr

    def plot_math_function(self, function_str):
        """
        Plots a mathematical function given as a string using Matplotlib.

        Parameters:
            function_str (str): The mathematical function to plot, in the form of a string.

        Returns:
            None

        The plot_math_function() function takes three parameters:

        function_str: The mathematical function to plot, as a string.
        x_range: The range of x values to plot, as a tuple (xmin, xmax).
        num_points: The number of points to plot.
        The function first generates an array of x values to plot using the np.linspace() function from the NumPy library. 
        This generates an array of num_points equally spaced values between x_range[0] and x_range[1].

        Next, the function creates a namespace for the math functions using a Python dictionary. This namespace will be used to evaluate the input function string. 
        The dictionary initially contains a single key-value pair with the variable x mapped to the array of x values generated in the previous step. 
        It then updates the dictionary with all the functions and constants in the math module using the math.__dict__ attribute.

        The eval() function is then used to evaluate the input function string in the context of the namespace dictionary. 
        The try-except block is used to catch any errors that may occur during evaluation, such as if the input 
        function string is invalid.

        Finally, the function creates a plot using the plt.plot() function from the Matplotlib library. The x and y values are passed as arguments to this
        """
        # Define the x values to plot
        x_vals = np.linspace(self.x_range[0], self.x_range[1], self.num_points)

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
        plt.plot(x_vals, y_vals, label=function_str, color=self.clr)

        # Add labels and title
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.title(function_str)
        plt.legend()

        # Show the plot
        plt.show()

function = graph_function(x_range=(-1000, 1000), num_points=1000, clr="r")
function.plot_math_function("x*3")
