from tkinter import messagebox, ttk
from typing import List
import matplotlib.pyplot as plt
import numpy as np
import math
import tkinter as tk
from random import randrange
import scipy.optimize as optimize
import os
from sympy import *



class GraphingCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Graphing Calculator")
        self.functions_dict = {}
        self.plot_dict = {}
        self.prev_line = None 

        self.intersected_lines_list = []

        master.resizable(True, True)
        master.minsize(300, 300)

        self.information_button = tk.Button(master, text="How to Use! (Info)", command=self.display_info)
        self.information_button.pack()
        
        # Create function input label and entry box
        self.function_label = tk.Label(master, text="Enter function")
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
        self.plot_button = tk.Button(master, text="plot function", command=self.plot_function)
        self.plot_button.pack()

        self.drop_menu_label = tk.Label(master, text="Menu: Extra Functions")
        self.drop_menu_label.pack()

        self.drop_menu_items = [
            "Select Options",
            "Annote/Track",
            "Intersect",
            "Derivative (dy/dx)",
            "Zero-Point",
            "Y-intercept",
            "Delete",
            "Return/Exit",
        ]

        self.drop_menu_variable = tk.StringVar(master)
        self.drop_menu_variable.set(self.drop_menu_items[0])
        self.drop_menu_variable.trace('w', self.menu_callback)

        self.drop_menu = ttk.OptionMenu(master, self.drop_menu_variable, *self.drop_menu_items)
        self.drop_menu.pack()

        self.fig, self.ax = plt.subplots()
        self.ax.grid()

         # Create a dot to track the mouse movement
        self.dot, = self.ax.plot([], [], 'o', markersize=7, color="black")
        
        # Create a text box to display the coordinates
        self.coord_text = self.ax.text(0.05, 0.95, "", transform=self.ax.transAxes, va='bottom')
        self.coord_visible = {line: False for line in self.plot_dict.values()}
        
        # Connect the mouse event handler functions to the plot
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_move)
    
  


    def on_click(self, event):        
        try:
            for line in self.plot_dict.values():
                if event.inaxes == self.ax and event.button == 1 and line.contains(event)[0]:
                    if self.menu_callback() == 1 or 3:
                        if line not in self.coord_visible:
                            self.coord_visible[line] = False

                    if self.menu_callback() == 2:
                        if line.contains(event)[0]:
                            if self.prev_line is not None:
                                # Compare the previously clicked line with the currently clicked line
                                if line != self.prev_line:
                                    messagebox.showinfo(title="Intersect", message="You Have Clicked on Two Functions")
                                    self.intersected_lines_list.append(line) 
                                    self.check_intersection()
                                    # Do something here to handle the intersection between two lines
                                    self.prev_line = None
                        
                            messagebox.showinfo(title="Intersect", message="You Have Clicked on One Functions")
                            self.prev_line = line
                            self.intersected_lines_list.append(self.prev_line)                                           
                        
                    if self.menu_callback() == 4:                      
                        # Get the x coordinate of the mouse cursor
                        x = event.xdata
                        # Get the y coordinate of the function at the given x value
                        y = line.get_ydata()[int((x - line.get_xdata()[0]) / (line.get_xdata()[1] - line.get_xdata()[0]))]

                        # Compute the zero point of the function using the secant method
                        x0, x1 = x, x + 0.01  # Initialize the secant method with two nearby points
                        eps = 1e-6  # Set a tolerance value for the root
                        while abs(x1 - x0) > eps:
                            y0, y1 = line.get_ydata()[int((x0 - line.get_xdata()[0]) / (line.get_xdata()[1] - line.get_xdata()[0]))], \
                                    line.get_ydata()[int((x1 - line.get_xdata()[0]) / (line.get_xdata()[1] - line.get_xdata()[0]))]
                            if abs(y1 - y0) < eps:
                                # If the function is nearly constant in the interval, stop the secant method
                                break
                            x0, x1 = x1, x1 - y1 * (x1 - x0) / (y1 - y0)  # Update the secant method
                        zero_point = x1

                        # Update the text box with the zero point of the function
                        self.coord_text.set_text(f"Zero point: x={zero_point:.2f}, y=0.00")
                        # Move the dot to the zero point of the function
                        self.dot.set_data(zero_point, 0)
                        # Redraw the plot to update the text box and dot
                        self.fig.canvas.draw()

                    if self.menu_callback() == 5:
                        for key, value in self.plot_dict.items():
                            if value == line:
                                expression = str(key)
                                expression_with_x_replaced = expression.replace("x", "0")
                                expression_with_x_replaced = eval(expression_with_x_replaced)

                                # Update the text box with the y-intercept of the function
                                self.coord_text.set_text(f"x=0.00, y={expression_with_x_replaced:.2f}")
                                # Move the dot to the y-intercept of the function
                                self.dot.set_data(0, expression_with_x_replaced)
                                # Redraw the plot to update the text box and dot
                                self.fig.canvas.draw()

                    
                    if self.menu_callback() == 6:
                        for key, value in self.plot_dict.items():
                            if value == line:
                                self.plot_dict[key].remove() 
                                del self.plot_dict[key]
                                del self.functions_dict[key]
                                self.ax.legend(loc="upper right")
                                self.fig.canvas.draw()

                    if self.menu_callback() == 7:
                        break  

                    self.coord_visible[line] = not self.coord_visible[line]
                    self.coord_text.set_visible(self.coord_visible[line])
                    self.dot.set_visible(self.coord_visible[line])
                    self.fig.canvas.draw()
                           
        except KeyError:
            pass
              

    
    # Define a function to handle mouse movement
    def on_move(self, event):
        # Loop over the line objects and check if the coordinate text box and dot are visible for each function
        try:
            for line in self.plot_dict.values():
                if event.inaxes == self.ax and self.coord_visible[line]:
                    if self.menu_callback() == 1:
                        # Get the x coordinate of the mouse cursor
                        x = event.xdata
                        # Compute the y coordinate of the function at the given x value
                        y = line.get_ydata()[int((x - line.get_xdata()[0]) / (line.get_xdata()[1] - line.get_xdata()[0]))]
                        # Update the text box with the coordinates of the function
                        self.coord_text.set_text(f"x={x:.2f}, y={y:.2f}")
                        # Move the dot to the point on the function
                        self.dot.set_data(x, y)
                        # Redraw the plot to update the text box and dot
                        self.fig.canvas.draw()

                    if self.menu_callback() == 3:
                        x = event.xdata
                        # Compute the y coordinate of the function at the given x value
                        y = line.get_ydata()[int((x - line.get_xdata()[0]) / (line.get_xdata()[1] - line.get_xdata()[0]))]
                        # Estimate the derivative using the central difference method
                        dx = (line.get_xdata()[1] - line.get_xdata()[0])
                        dy = line.get_ydata()[int((x - line.get_xdata()[0]) / dx) + 1] - line.get_ydata()[int((x - line.get_xdata()[0]) / dx)]
                        deriv = dy / dx
                        # Update the text box with the coordinates and derivative of the function
                        self.coord_text.set_text(f"x={x:.2f}, y={y:.2f}, dy/dx={deriv:.2f}")
                        # Move the dot to the point on the function
                        self.dot.set_data(x, y)
                        # Redraw the plot to update the text box and dot
                        self.fig.canvas.draw()
    
        except KeyError:
            pass

  
    def menu_callback(self, *args):
        selection = self.drop_menu_variable.get()
        selected_index = self.drop_menu_items.index(selection)
        return selected_index

    def check_intersection(self):
            # Get all visible lines     
            print(self.intersected_lines_list)

            for key, value in self.plot_dict.items():
                if value == self.intersected_lines_list[0]:
                    self.intersected_lines_list[0] = str(key)
                elif value == self.intersected_lines_list[1]:
                    self.intersected_lines_list[1] = str(key)
                else:
                    pass


            if len(self.intersected_lines_list) == 2:       
                x = symbols('x')
                f1 = eval(self.intersected_lines_list[0])
                f2 = eval(self.intersected_lines_list[1])

                intersection_points = solve(f1 - f2, x)
                print(intersection_points)

                intersection_points = [str(x) for x in intersection_points]
        
                for i in range(len(intersection_points)):
                    expression_with_x_replaced = self.intersected_lines_list[0].replace("x", intersection_points[i])
                    expression_with_x_replaced = eval(expression_with_x_replaced)
                  
                    dots, = self.ax.plot(eval(intersection_points[i]), expression_with_x_replaced, marker='o', linestyle='none', color='black')
                    self.ax.text(eval(intersection_points[i]) + 0.1, expression_with_x_replaced + 0.1, f'Dot {i+1}: ({eval(intersection_points[i])}, {expression_with_x_replaced})')
                    self.fig.canvas.draw() 
            

                self.intersected_lines_list.clear()
                self.prev_line = None

                   

    def display_info(self):
        messagebox.showinfo(title="Hello! How to Enter Functions", 
        message="Welcome to the app: This is a Graphcalculator, you enter the function y = 2x^2 as in said format i.e, 2*x**2. You enter trig/log funtions as such sin(x) or log(x) or ln(x). There additional options below, where you can track, derive and etc, in which you can access through clicking")

    def random_color(self):
      r = randrange(255)
      g = randrange(255)
      b = randrange(255)
      return "#{:02x}{:02x}{:02x}".format(r, g, b)
    
    def bounds_check(self, lower, upper):
        if float(lower) < float(upper): 
            self.ax.set_xlim(lower, upper)
            return True
        else:
            return False
        
    def is_constant_function(self, expression): 
        try:
            constants = {'e': math.e, 'pi': math.pi,
                        'exp': np.exp, 'sin': np.sin,
                        'cos': np.cos,'tan': np.tan,
                        'log': np.log10, 'ln': np.log,
                        'sqrt': np.sqrt, "arcsin": np.arcsin,
                        "arccos": np.arccos, "arctan": np.arctan, }
            return eval(expression, constants)
        except:
            return None 
    
    def plot_function(self):
        # Get function string and x range from entry boxes
        if self.x_min_entry.get() and self.x_max_entry.get():
            try:
                x_min = float(self.x_min_entry.get())
                x_max = float(self.x_max_entry.get())
            except ValueError:
                messagebox.showerror(title="Error", message="Invalid X Values")
                return
        else:
            messagebox.showerror(title="Error", message="Please Enter X Values: X-value have been set to default x-min: -10 and x-max: 10.")
            x_min = float(-10)
            x_max = float(10)
             

        if self.y_min_entry.get() and self.y_max_entry.get():
            try:
                y_min = float(self.y_min_entry.get())
                y_max = float(self.y_max_entry.get())
            except ValueError:
                messagebox.showerror(title="Error", message="Invalid Y Values.")
                return
        else:
            messagebox.showerror(title="Error", message="Please Enter Y Values: : Y-value have been set to default y-min: -10 and y-max: 10.")
            y_min = float(-10)
            y_max = float(10)
            

        if (self.bounds_check(lower=x_min, upper=x_max) and self.bounds_check(lower=y_min, upper=y_max)) == True:
            function_str = self.function_entry.get()
            clr = self.random_color()
            num_points = 10000

            x_vals = np.linspace(x_min, x_max, num_points)
            namespace = {'x': x_vals}
            namespace.update(math.__dict__)
            namespace.update({'exp': np.exp, 'sin': np.sin, 
                            'cos': np.cos, 'tan': np.tan,
                            'log': np.log10, 'ln': np.log, 
                            'sqrt': np.sqrt, "arcsin": np.arcsin,
                            "arccos": np.arccos, "arctan": np.arctan, }) # type: ignore
               
            if function_str in self.functions_dict:
                for keys in self.plot_dict.keys():
                    self.plot_dict[keys].remove() 
                   
                for keys in self.plot_dict.keys():
                    if self.is_constant_function(function_str) is not None:
                        x_vals = np.linspace(x_min, x_max, 2)
                        y_vals = np.full(2, self.is_constant_function(keys))
                    else:
                        try:
                            y_vals = eval(keys, namespace)
                        except:
                            return
            
                    handle, = self.ax.plot(x_vals, y_vals, label=keys, color=self.functions_dict[keys])
                    self.plot_dict[keys] = handle
                messagebox.showerror(title="Error", message=f"Function {function_str} is already on the plot")

            elif len(function_str) == 0 and len(self.plot_dict) != 0:
                for keys in self.plot_dict.keys():
                    self.plot_dict[keys].remove()
                
                for keys in self.plot_dict.keys():
                    if self.is_constant_function(function_str) is not None:
                        x_vals = np.linspace(x_min, x_max, 2)
                        y_vals = np.full(2, self.is_constant_function(keys))
                    else:
                        try:
                            y_vals = eval(keys, namespace)
                        except:
                            return
            
                    handle, = self.ax.plot(x_vals, y_vals, label=keys, color=self.functions_dict[keys])
                    self.plot_dict[keys] = handle

            elif self.is_constant_function(function_str) is not None:
                x_vals = np.linspace(x_min, x_max, 2)
                y_vals = np.full(2, self.is_constant_function(function_str))
                handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
                self.functions_dict[function_str] = clr
                self.plot_dict[function_str] = handle

            else:
     
                try:
                    y_vals = eval(function_str, namespace)
                    self.bool_value = True
                except:    
                    messagebox.showerror(title="Error", message="Invalid function.")
                    print("Invalid function.")
                    self.bool_value =  False
                    return
                
                if self.bool_value != False and len(function_str) > 0:
                    handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
                    self.functions_dict[function_str] = clr
                    self.plot_dict[function_str] = handle
                    self.bool_value = True
                else: 
                    pass
  
            print(self.plot_dict)
            print(self.functions_dict)
            self.ax.set_xlim(xmin=x_min, xmax=x_max)
            self.ax.set_ylim(ymin=y_min, ymax=y_max)
            self.ax.spines["left"].set_position("zero") #type:ignore
            self.ax.spines["bottom"].set_position("zero") #type: ignore 
            self.ax.spines["right"].set_visible(False) #type:ignore
            self.ax.spines["top"].set_visible(False)
            self.master.after(100, self.master.update)  # force update the window to show the plot
            self.ax.legend(loc="upper right")
            plt.ion()
            plt.show()

        else:
            messagebox.showerror(title="Error: Invalid Values", message="Check Values for x_min, x_max, y_min, y_max.")
            return

root = tk.Tk()
graphing_calculator = GraphingCalculator(root)
root.mainloop()
