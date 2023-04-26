from tkinter import messagebox
from typing import List
import matplotlib.pyplot as plt
import numpy as np
import math
import tkinter as tk
from random import randrange

class GraphingCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Graphing Calculator")
        # self.functions_list: List[str] = []  # list of plotted function strings
        self.functions_dict = {}
        self.plot_dict = {}


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

      
        # Create plot button
        self.plot_button = tk.Button(master, text="plot", command=self.plot_function)
        self.plot_button.pack()

        self.fig, self.ax = plt.subplots()
        self.ax.grid()

   
    def sort_function_list(self, input):
        list1 = []
        [list1.append(x) for x in input if x not in list1]
        return list1

    def random_color(self):
      r = randrange(255)
      g = randrange(255)
      b = randrange(255)
      return "#{:02x}{:02x}{:02x}".format(r, g, b)
    
  
          
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
                'sqrt': np.sqrt,
                "arcsin": np.arcsin,
                "arccos": np.arccos,
                "arctan": np.arctan, 

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
        if self.x_min_entry.get() and self.x_max_entry.get():
            try:
                x_min = float(self.x_min_entry.get())
                x_max = float(self.x_max_entry.get())
            except ValueError:
                messagebox.showerror(title="Error", message="Invalid x Values.")
                return
        else:
            messagebox.showerror(title="Error", message="Please Enter x Values.")
            return

        if self.y_min_entry.get() and self.y_max_entry.get():
            try:
                y_min = float(self.y_min_entry.get())
                y_max = float(self.y_max_entry.get())
            except ValueError:
                messagebox.showerror(title="Error", message="Invalid y Values.")
                return
        else:
            messagebox.showerror(title="Error", message="Please Enter y Values.")
            return


        function_str = self.function_entry.get()
        clr = self.random_color()
        num_points = 10000

        x_vals = np.linspace(x_min, x_max, num_points)
        namespace = {'x': x_vals}
        namespace.update(math.__dict__)
        namespace.update({'exp': np.exp, 'sin': np.sin, 
                        'cos': np.cos, 'tan': np.tan,
                        'log': np.log10, 'ln': np.log, 
                        'sqrt': np.sqrt,
                        "arcsin": np.arcsin,
                        "arccos": np.arccos,
                        "arctan": np.arctan, }) # type: ignore
        
        if function_str in self.functions_dict:
            messagebox.showerror(title="Error", message=f"Function {function_str} is already on the plot")

            for keys in self.plot_dict.keys():
                self.plot_dict[keys].remove()
            
            for keys in self.plot_dict.keys():
                try:
                    y_vals = eval(keys, namespace)
                except:
                      return
              
                handle, = self.ax.plot(x_vals, y_vals, label=keys, color=self.functions_dict[keys])
                self.plot_dict[keys] = handle

                



        elif self.is_constant_function(function_str) is not None:
              x_vals = np.linspace(x_min, x_max, num_points)
              y_vals = np.full(2, self.is_constant_function(function_str))
              handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
              self.functions_dict[function_str] = clr
              self.plot_dict[function_str] = handle


        else:
          try:
              y_vals = eval(function_str, namespace)
          except:
              messagebox.showerror(title="Error", message="Invalid function.")
              print("Invalid function.")
              return
      
          handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
          self.functions_dict[function_str] = clr
          self.plot_dict[function_str] = handle

      



        
        print(self.functions_dict)
    
        self.ax.set_xlim(x_min, x_max)  
        self.ax.set_ylim(y_min, y_max)
        self.ax.spines["left"].set_position("zero") #type:ignore
        self.ax.spines["bottom"].set_position("zero") #type: ignore 
        self.ax.spines["right"].set_visible(False) #type:ignore
        self.ax.spines["top"].set_visible(False)
        self.master.after(100, self.master.update)  # force update the window to show the plot
        self.ax.legend()
        plt.ion()

        plt.show()

      


root = tk.Tk()
graphing_calculator = GraphingCalculator(root)
root.mainloop()
