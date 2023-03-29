from tkinter import messagebox
from typing import List
import matplotlib.pyplot as plt
import numpy as np
import math
import tkinter as tk

class GraphingCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Graphing Calculator")
        self.plot_handles = {}  # keep track of plotted functions and their colors
        self.functions_list: List[str] = []  # list of plotted function strings

        master.resizable(True, True)
        master.minsize(300, 300)

        # Create function input label and entry box
        self.function_label = tk.Label(master, text="function")
        self.function_label.pack()
        self.function_entry = tk.Entry(master)
        self.function_entry.pack()

        # Create x range input label and entry boxes
        self.x_min_label = tk.Label(master, text="x-min: ")
        self.x_min_label.pack()
        self.x_min_entry = tk.Entry(master)
        self.x_min_entry.pack()

        self.x_max_label = tk.Label(master, text="x-max: ")
        self.x_max_label.pack()
        self.x_max_entry = tk.Entry(master)
        self.x_max_entry.pack()

        # Create y range input label and entry boxes
        self.y_min_label = tk.Label(master, text="y-min: ")
        self.y_min_label.pack()
        self.y_min_entry = tk.Entry(master)
        self.y_min_entry.pack()

        self.y_max_label = tk.Label(master, text="y-max: ")
        self.y_max_label.pack()
        self.y_max_entry = tk.Entry(master)
        self.y_max_entry.pack()

        # Create color input label and entry box
        self.color_label = tk.Label(master, text="color: ")
        self.color_label.pack()
        self.color_entry = tk.Entry(master)
        self.color_entry.pack()

        # Create plot button
        self.plot_button = tk.Button(master, text="plot", command=self.plot_function)
        self.plot_button.pack()
        
        self.fig, self.ax = plt.subplots()
        self.ax.grid()
    
    def is_constant_function(self, function_str):
        try:
            namespace = {
                'pi': math.pi,
                'e': math.e,
                'exp': np.exp,
                'sin': np.sin,
                'cos': np.cos,
                'tan': np.tan,
                'log': np.log10,
                'ln': np.log,
                'sqrt': np.sqrt
            }
            namespace.update(math.__dict__)
            c = eval(function_str, namespace)
            if isinstance(c, (int, float)):
                return c
            else:
                return None
        except:
            return None


    def plot_function(self):
        # Get function string and x range from entry boxes
        function_str = self.function_entry.get()
        x_min = float(self.x_min_entry.get())
        x_max = float(self.x_max_entry.get())
        x_range = (x_min, x_max)

        y_min = float(self.y_min_entry.get())
        y_max = float(self.y_max_entry.get())

        clr = str(self.color_entry.get())

        num_points = 1000

        # self.ax.set_xbound(x_min, x_max)
        # self.ax.set_ybound(y_min, y_max)

        x1 = [i for i in range(int(x_min), int(x_max))] # type: ignore
        y1 = [i for i in range(int(y_min), int(y_max))] # type: ignore

        tick_range_x = len(x1)
        tick_range_y = len(y1)
      
        # Set the ticks
        self.ax.set_xticks(np.linspace(x_min, x_max, tick_range_x+1))
        self.ax.set_yticks(np.linspace(y_min, y_max, tick_range_y+1))

        # Check if the function has already been plotted
        if function_str in self.plot_handles:
            # Update the color of the existing plot
            handle = self.plot_handles[function_str]
            handle.set_color(clr)
            messagebox.showwarning(title="Warning", message="The function already exists")
        if self.is_constant_function(function_str) is not None and function_str not in self.plot_handles:
            x_vals = np.linspace(x_min, x_max, 2)
            y_vals = np.full(2, self.is_constant_function(function_str))
            handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
            self.plot_handles[function_str] = handle
            self.functions_list.append(function_str) 
        else:
            
            x_vals = np.linspace(x_range[0], x_range[1], num_points)

            # Create a namespace for the math functions
            namespace = {'x': x_vals}
            namespace.update(math.__dict__)
            namespace.update({'exp': np.exp, 'sin': np.sin, 
                            'cos': np.cos, 'tan': np.tan,
                            'log': np.log10, 'ln': np.log, 
                            'sqrt': np.sqrt}) # type: ignore

            # Evaluate the function for each x value
            try:
                y_vals = eval(function_str, namespace)
            except:
                messagebox.showerror(title="Error", message="Invalid function.")
                print("Invalid function.")
                return

        if function_str not in self.plot_handles:
            # Create the plot
            handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
            self.plot_handles[function_str] = handle
            self.functions_list.append(function_str) 
            print(self.plot_handles)
        else:
            pass
        

        # Add labels and title
        # plt.xlabel("X-Axis")
        # plt.ylabel("Y-Axis")

        self.ax.set_xlim(xmin=x_min, xmax=x_max)  
        self.ax.set_ylim(ymin=y_min, ymax=y_max)
        self.ax.spines["left"].set_position("zero") #type:ignore
        self.ax.spines["bottom"].set_position("zero") #type:ignore
        self.ax.spines["right"].set_visible(False) #type:ignore
        self.ax.spines["top"].set_visible(False) #type:ignore

        self.ax.legend()    
        # Show the plot
        plt.show()

    


root = tk.Tk()
graphing_calculator = GraphingCalculator(root)
root.mainloop()
