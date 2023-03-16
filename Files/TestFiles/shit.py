# import matplotlib.pyplot as plt

# def plot_hover():
#     fig, ax = plt.subplots()

#     # Define the coordinates of the plot
#     x = [1, 2, 3, 4, 5]
#     y = [2, 4, 6, 8, 10]

#     # Plot the data
#     ax.plot(x, y)

#     # Define a function to handle mouse movement events
#     def on_hover(event):
#         if event.inaxes == ax:
#             x = event.xdata
#             y = event.ydata
#             print(f'x={x:.2f}, y={y:.2f}')

#     # Connect the function to the mouse movement event
#     fig.canvas.mpl_connect('motion_notify_event', on_hover)

#     plt.show()

# plot_hover()


"""
This can write show the coordinate of one function at least
"""
# import matplotlib.pyplot as plt

# class PlotTracker:
#     def __init__(self, x, y):
#         self.fig, self.ax = plt.subplots()
#         self.x = x
#         self.y = y
#         self.current_point = None
#         self.plot_line, = self.ax.plot(x, y)
#         self.annotation = self.ax.annotate("", xy=(0,0), xytext=(-20,20),
#                 textcoords="offset points",
#                 bbox=dict(boxstyle="round", fc="w"),
#                 arrowprops=dict(arrowstyle="->"))
#         self.annotation.set_visible(False)
#         self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)
#         self.fig.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
#         plt.show()

#     def on_key_press(self, event):
#         if event.key == ' ':
#             if self.current_point is None:
#                 self.current_point, = self.ax.plot(self.x[0], self.y[0], 'o', color='red')
#             else:
#                 self.current_point.remove()
#                 self.current_point = None

#     def on_mouse_move(self, event):
#         if event.inaxes == self.ax:
#             if self.current_point is not None:
#                 x, y = event.xdata, event.ydata
#                 x, y = self.get_closest_point(x, y)
#                 self.current_point.set_data(x, y)
#                 self.annotation.xy = x, y # type: ignore
#                 self.annotation.set_text(f'x={x:.2f}, y={y:.2f}')
#                 self.annotation.set_visible(True)
#                 self.fig.canvas.draw_idle()

#     def get_closest_point(self, x, y):
#         distances = [(xi - x)**2 + (yi - y)**2 for xi, yi in zip(self.x, self.y)]
#         closest_idx = min(range(len(distances)), key=distances.__getitem__)
#         return self.x[closest_idx], self.y[closest_idx]

# # Define the coordinates of the plot
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# # Create a plot tracker object
# tracker = PlotTracker(x, y)

"""
Failed annote function
"""

#  handle, = plt.plot(self.x_vals, self.y_vals, label=function_str, color=clr)
#         # Add the hover functionality
#         def on_hover(event):
#             if event.inaxes is not None and event.inaxes.get_lines():
#                 line = event.inaxes.get_lines()[0]
#                 xdata = line.get_xdata()
#                 ydata = line.get_ydata()
#                 x, y = event.xdata, event.ydata
#                 index = find_nearest_index(xdata, x)
#                 x_val, y_val = xdata[index], ydata[index]
#                 plt.title(f"({x_val:.2f}, {y_val:.2f})")
#                 plt.draw()

#         def on_press(event):
#             if event.inaxes is not None and event.inaxes.get_lines():
#                 line = event.inaxes.get_lines()[0]
#                 xdata = line.get_xdata()
#                 ydata = line.get_ydata()
#                 x, y = event.xdata, event.ydata
#                 index = find_nearest_index(xdata, x)
#                 x_val, y_val = xdata[index], ydata[index]
#                 plt.title(f"({x_val:.2f}, {y_val:.2f})")
#                 plt.draw()
#                 fig.canvas.mpl_disconnect(hover_cid)
#                 fig.canvas.mpl_connect('motion_notify_event', on_move)

#         def on_move(event):
#             if event.inaxes is not None and event.inaxes.get_lines():
#                 line = event.inaxes.get_lines()[0]
#                 xdata = line.get_xdata()
#                 ydata = line.get_ydata()
#                 x, y = event.xdata, event.ydata
#                 index = find_nearest_index(xdata, x)
#                 x_val, y_val = xdata[index], ydata[index]
#                 plt.title(f"({x_val:.2f}, {y_val:.2f})")
#                 plt.draw()

#         fig = plt.gcf()
#         hover_cid = fig.canvas.mpl_connect('motion_notify_event', on_hover)
#         press_cid = fig.canvas.mpl_connect('button_press_event', on_press)

#         self.plot_handles[function_str] = handle

        

#         def find_nearest_index(array, value):
#             return np.abs(array - value).argmin()
    
#     # Add labels and title
#         plt.xlabel("X-Axis")
#         plt.ylabel("Y-Axis")
#         plt.legend()


"""
Toggles between different graphs with different plots
"""
# import numpy as np
# import matplotlib.pyplot as plt

# # Define the functions to plot
# x = np.linspace(-10, 10, 1000)
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = np.tan(x)

# # Create the initial plot of the first function
# fig, ax = plt.subplots()
# line, = ax.plot(x, y1)

# # Define a list of the functions to toggle between
# functions = [y1, y2, y3]
# function_names = ['y=sin(x)', 'y=cos(x)', 'y=tan(x)']
# current_function = 0

# # Define a function to toggle between the different functions
# def toggle_function(event):
#     global current_function
#     if event.key == 'tab':
#         current_function = (current_function + 1) % len(functions)
#         line.set_ydata(functions[current_function])
#         ax.set_title(function_names[current_function])
#         fig.canvas.draw()

# # Connect the toggle_function function to the key press event
# fig.canvas.mpl_connect('key_press_event', toggle_function)

# # Define a function to track the mouse movement and show the trajectory of the graph
# def track_mouse(event):
#     if event.inaxes:
#         x, y = event.xdata, event.ydata
#         ax.set_title(f'{function_names[current_function]} | x={x:.2f}, y={y:.2f}')
#         fig.canvas.draw()

# # Connect the track_mouse function to the mouse movement event
# fig.canvas.mpl_connect('motion_notify_event', track_mouse)

# # Show the plot
# plt.show()

"""
Constant sheit
"""
# import re
# import math

# class GraphingCalculator:
#     # ... existing code ...
    
    # def is_constant_function(self, function_str):
    #     # Check if the function string is a constant number
    #     try:
    #         c = float(function_str)
    #         return True
    #     except:
    #         pass
        
    #     # Check if the function string is a constant expression with trigonometric functions
    #     trig_pattern = r"^(sin|cos|tan|cot|sec|csc)\(\s*(-?\d+(\.\d+)?)\s*\)$"
    #     match = re.match(trig_pattern, function_str)
    #     if match:
    #         return True
        
    #     # Check if the function string is a constant expression with logarithmic functions
    #     log_pattern = r"^(log|ln)\(\s*(-?\d+(\.\d+)?)\s*\)$"
    #     match = re.match(log_pattern, function_str)
    #     if match:
    #         return True
        
    #     # Check if the function string is a constant expression with exponential functions
    #     exp_pattern = r"^(exp)\(\s*(-?\d+(\.\d+)?)\s*\)$"
    #     match = re.match(exp_pattern, function_str)
    #     if match:
    #         return True
        
    #     # Check if the function string is a constant expression with radical functions
    #     rad_pattern = r"^(sqrt)\(\s*(-?\d+(\.\d+)?)\s*\)$"
    #     match = re.match(rad_pattern, function_str)
    #     if match:
    #         return True
        
    #     # If none of the above conditions were met, return False
    #     return False

"""
Constant sheit more
"""

 # def is_constant_function(self, function_str):
    #     try:
    #         c = float(function_str)
    #         return True
    #     except:
    #         return False

    # def is_constant_function(self, function_str):
    #     try:
    #         # Check if the function is a constant value
    #         c = float(function_str)
    #         return True
    #     except ValueError:
    #         pass

    #     # Check if the function is a trigonometric constant
    #     trig_constants = ['pi', 'e']
    #     for constant in trig_constants:
    #         if function_str == 'sin({})'.format(constant) or function_str == 'cos({})'.format(constant) or \
    #             function_str == 'tan({})'.format(constant) or function_str == 'cosec({})'.format(constant) or \
    #             function_str == 'sec({})'.format(constant) or function_str == 'cot({})'.format(constant):
    #             return True

    #     # Check if the function is a logarithmic constant
    #     log_constants = ['e', '2']
    #     for constant in log_constants:
    #         if function_str == 'log({})'.format(constant) or function_str == 'ln({})'.format(constant):
    #             return True

    #     # Check if the function is an exponential constant
    #     if function_str == 'exp(1)' or function_str == 'exp(2)':
    #         return True

    #     # Check if the function is a radical constant
    #     radical_constants = ['2', '3']
    #     for constant in radical_constants:
    #         if function_str == 'sqrt({})'.format(constant):
    #             return True

    #     # If the function is not a constant function
    #     return False

"""
More Constant sheit
"""

#  def is_constant_function(self, function_str):
#         try:
#             # Check for trig functions with constant argument
#             if 'sin(' in function_str or 'cos(' in function_str or 'tan(' in function_str:
#                 arg_start = function_str.index('(') + 1
#                 arg_end = function_str.index(')')
#                 arg = function_str[arg_start:arg_end]
#                 float(arg)
#                 return True
#             # Check for logarithmic functions with constant base and argument
#             elif 'log(' in function_str or 'ln(' in function_str:
#                 base = 10 if 'log(' in function_str else math.e
#                 arg_start = function_str.index('(') + 1
#                 arg_end = function_str.index(')')
#                 arg = function_str[arg_start:arg_end]
#                 float(arg)
#                 float(base)
#                 return True
#             # Check for exponential functions with constant base and argument
#             elif 'exp(' in function_str:
#                 arg_start = function_str.index('(') + 1
#                 arg_end = function_str.index(')')
#                 arg = function_str[arg_start:arg_end]
#                 float(arg)
#                 return True
#             # Check for radical functions with constant argument
#             elif 'sqrt(' in function_str:
#                 arg_start = function_str.index('(') + 1
#                 arg_end = function_str.index(')')
#                 arg = function_str[arg_start:arg_end]
#                 float(arg)
#                 return True
#             # Check for constant value
#             else:
#                 float(function_str)
#                 return True
#         except:
#             return False

# # get input from user
# input_string = input("Enter a mathematical expression: ")

# # evaluate the expression using eval() function
# result = eval(input_string)

# # print the result
# print("The result of the expression is:", result)

# import matplotlib.pyplot as plt
# import numpy as np
# import math
# import tkinter as tk
# from tkinter import messagebox
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# class GraphingCalculator:
#     def __init__(self, master):
#         self.master = master
#         master.title("Graphing Calculator")
#         self.plot_handles = []  # keep track of plotted functions and their colors
#         self.current_plot = 0   # index of current plot
#         self.fig, self.ax = plt.subplots()
#         self.canvas = FigureCanvasTkAgg(self.fig, master=master)
#         self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
#         self.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)

#         master.resizable(True, True)
#         master.minsize(300, 300)

#         # Create function input label and entry box
#         self.function_label = tk.Label(master, text="function")
#         self.function_label.pack()
#         self.function_entry = tk.Entry(master)
#         self.function_entry.pack()

#         # Create x range input label and entry boxes
#         self.x_min_label = tk.Label(master, text="x-min: ")
#         self.x_min_label.pack()
#         self.x_min_entry = tk.Entry(master)
#         self.x_min_entry.pack()

#         self.x_max_label = tk.Label(master, text="x-max: ")
#         self.x_max_label.pack()
#         self.x_max_entry = tk.Entry(master)
#         self.x_max_entry.pack()

#         # Create color input label and entry box
#         self.color_label = tk.Label(master, text="color: ")
#         self.color_label.pack()
#         self.color_entry = tk.Entry(master)
#         self.color_entry.pack()

#         # Create plot button
#         self.plot_button = tk.Button(master, text="plot", command=self.plot_function)
#         self.plot_button.pack()

#         # Create coordinates display box
#         self.coord_text = tk.StringVar()
#         self.coord_label = tk.Label(master, textvariable=self.coord_text)
#         self.coord_label.pack()

#         # Bind the tab key to toggle between plots
#         master.bind('<Tab>', self.toggle_plot)

#     def toggle_plot(self, event):
#         if len(self.plot_handles) > 1:
#             self.current_plot = (self.current_plot + 1) % len(self.plot_handles)
#             self.update_plot()

#     def update_plot(self):
#         self.ax.clear()
#         handle = self.plot_handles[self.current_plot]
#         self.ax.plot(handle['x_vals'], handle['y_vals'], label=handle['function'], color=handle['color'])
#         plt.xlabel("X-Axis")
#         plt.ylabel("Y-Axis")
#         plt.legend()
#         self.canvas.draw()

#     def on_mouse_move(self, event):
#         if event.inaxes
