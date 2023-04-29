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

# # Define the x values to plot
# if num_points < 1000:
#     num_points = 1000
# else:
#     num_points = abs(int(x_range[0])) + abs(int(x_range[1]))

# import matplotlib.pyplot as plt

"""
Ticks scaling i guess
"""

# fig, ax = plt.subplots()

# # turn on the grid and set its color
# ax.grid(True, color='gray')

# # set the tick positions and labels
# ax.set_xticks([0, 1, 2])
# ax.set_xticklabels(['A', 'B', 'C'])
# ax.set_yticks([0, 1, 2])
# ax.set_yticklabels(['X', 'Y', 'Z'])

# # set the tick positions and labels to be centered
# ax.tick_params(axis='both', which='both', direction='in', pad=10)
# ax.xaxis.set_ticks_position('both')
# ax.xaxis.set_label_position('bottom')
# ax.yaxis.set_ticks_position('both')
# ax.yaxis.set_label_position('left')

# # set the axis limits
# ax.set_xlim([-0.5, 2.5]) # type: ignore
# ax.set_ylim([-0.5, 2.5]) # type: ignore

# plt.show()

      # # Get function string and x range from entry boxes
      #   function_str = self.function_entry.get()
      #   x_min = float(self.x_min_entry.get())
      #   x_max = float(self.x_max_entry.get())
      #   x_range = (x_min, x_max)

      #   y_min = float(self.y_min_entry.get())
      #   y_max = float(self.y_max_entry.get())

      #   clr = str(self.color_entry.get())

      #   num_points = 1000

      #   self.ax.set_xbound(x_min, x_max)
      #   self.ax.set_ybound(y_min, y_max)

      #   # Check if the function has already been plotted
      #   if function_str in self.plot_handles:
      #       # Update the color of the existing plot
      #       handle = self.plot_handles[function_str]
      #       handle.set_color(clr)
      #       messagebox.showwarning(title="Warning", message="The function already exists")
      #   if self.is_constant_function(function_str) is not None and function_str not in self.plot_handles:
      #       x_vals = np.linspace(x_min, x_max, 2)
      #       y_vals = np.full(2, self.is_constant_function(function_str))
      #       handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
      #       self.plot_handles[function_str] = handle
      #       self.functions_list.append(function_str) 
      #   else:
            
      #       x_vals = np.linspace(x_range[0], x_range[1], num_points)

      #       # Create a namespace for the math functions
      #       namespace = {'x': x_vals}
      #       namespace.update(math.__dict__)
      #       namespace.update({'exp': np.exp, 'sin': np.sin, 
      #                       'cos': np.cos, 'tan': np.tan,
      #                       'log': np.log10, 'ln': np.log, 
      #                       'sqrt': np.sqrt}) # type: ignore

      #       # Evaluate the function for each x value
      #       try:
      #           y_vals = eval(function_str, namespace)
      #       except:
      #           messagebox.showerror(title="Error", message="Invalid function.")
      #           print("Invalid function.")
      #           return

      #   if function_str not in self.plot_handles:
      #       # Create the plot
      #       handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
      #       self.plot_handles[function_str] = handle
      #       self.functions_list.append(function_str) 
      #       print(self.plot_handles)
      #   else:
      #       pass

      #   # Set the ticks on the x and y axes
      #   self.ax.set_xticks(np.linspace(x_min, x_max, 5))
      #   self.ax.set_yticks(np.linspace(y_min, y_max, 5))

      #   # Add labels and title
      #   self.ax.set_xlabel("X-Axis")
      #   self.ax.set_ylabel("Y-Axis")
      #   self.ax.set_title("Graph")

      #   self.ax.legend()

      #   # Show the plot
      #   plt.show()


      #       # Add labels and title
      #       # plt.xlabel("X-Axis")
      #       # plt.ylabel("Y-Axis")
      #       self.ax.legend()    
      #       # Show the plot
      #       plt.show()


"""
Change window function
"""       
# def change_graph_window(self):
#       x_min = float(self.x_min_entry.get())
#       x_max = float(self.x_max_entry.get())

#       y_min = float(self.y_min_entry.get())
#       y_max = float(self.y_max_entry.get())

#       x1 = [i for i in range(int(x_min), int(x_max))] # type: ignore
#       y1 = [i for i in range(int(y_min), int(y_max))] # type: ignore

#       tick_range_x = len(x1)
#       tick_range_y = len(y1)

#       # Set the ticks
#       self.ax.set_xticks(np.linspace(x_min, x_max, tick_range_x+1))
#       self.ax.set_yticks(np.linspace(y_min, y_max, tick_range_y+1))

#       self.ax.set_xlim(xmin=x_min, xmax=x_max)  
#       self.ax.set_ylim(ymin=y_min, ymax=y_max)

#       plt.show()

"""
Update all graph function if new x_min and x_max
"""

# def plot_function(self):
#         # Get function string and x range from entry boxes
#         function_str = self.function_entry.get()

#         if float(self.x_min_entry.get()) or float(self.x_min_entry.get()) != ValueError:
#           x_min = float(self.x_min_entry.get())
#           x_max = float(self.x_max_entry.get())
#         else:
#           x_min = float(-10)
#           x_max = float(10)

#         x_range = (x_min, x_max)

#         y_min = float(self.y_min_entry.get())
#         y_max = float(self.y_max_entry.get())

#         clr = str(self.color_entry.get())

#         num_points = 1000

    
#         # Check if the function has already been plotted
#         if function_str in self.plot_handles:
#             # Update the color and x range of the existing plot
#             handle = self.plot_handles[function_str]
#             handle.set_color(clr)
#             x_vals = np.linspace(x_min, x_max, num_points)
#             y_vals = eval(function_str, {'x': x_vals, 'pi': math.pi, 'e': math.e})
#             handle.set_xdata(x_vals)
#             handle.set_ydata(y_vals)
#             messagebox.showwarning(title="Warning", message="The function already exists")
#             self.ax.relim()
#             self.ax.autoscale_view()
#         elif self.is_constant_function(function_str) is not None:
#             x_vals = np.linspace(x_min, x_max, 2)
#             y_vals = np.full(2, self.is_constant_function(function_str))
#             handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
#             self.plot_handles[function_str] = handle
#             self.functions_list.append(function_str) 
#         else:
#             x_vals = np.linspace(x_range[0], x_range[1], num_points)

#             # Create a namespace for the math functions
#             namespace = {'x': x_vals}
#             namespace.update(math.__dict__)
#             namespace.update({'exp': np.exp, 'sin': np.sin, 
#                             'cos': np.cos, 'tan': np.tan,
#                             'log': np.log10, 'ln': np.log, 
#                             'sqrt': np.sqrt}) # type: ignore

#             # Evaluate the function for each x value
#             try:
#                 y_vals = eval(function_str, namespace)
#             except:
#                 messagebox.showerror(title="Error", message="Invalid function.")
#                 print("Invalid function.")
#                 return

#             # Create the plot
#             handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
#             self.plot_handles[function_str] = handle
#             self.functions_list.append(function_str) 

#         self.ax.set_xlim(xmin=x_min, xmax=x_max)  
#         self.ax.set_ylim(ymin=y_min, ymax=y_max)
#         self.ax.spines["left"].set_position("zero") #type:ignore
#         self.ax.spines["bottom"].set_position("zero") #type:ignore
#         self.ax.spines["right"].set_visible(False) #type:ignore
#         self.ax.spines["top"].set_visible(False) #type:ignore
#         self.ax.legend()
#         self.fig.canvas.draw()
      
#         plt.show()

"""
Proper plot_function
"""

   # def plot_function(self):
    #     # Get function string and x range from entry boxes
    #     function_str = self.function_entry.get()

    #     if float(self.x_min_entry.get()) or float(self.x_min_entry.get()) != ValueError:
    #       x_min = float(self.x_min_entry.get())
    #       x_max = float(self.x_max_entry.get())
    #     else:
    #       x_min = float(-10)
    #       x_max = float(10)


    #     x_range = (x_min, x_max)

    #     y_min = float(self.y_min_entry.get())
    #     y_max = float(self.y_max_entry.get())

    #     clr = str(self.color_entry.get())

    #     num_points = 1000

    
    #     # Check if the function has already been plotted
    #     if function_str in self.plot_handles:
    #         # Update the color of the existing plot
    #         handle = self.plot_handles[function_str]
    #         handle.set_color(clr)
    #         messagebox.showwarning(title="Warning", message="The function already exists")
    #     if self.is_constant_function(function_str) is not None and function_str not in self.plot_handles:
    #         x_vals = np.linspace(x_min, x_max, 2)
    #         y_vals = np.full(2, self.is_constant_function(function_str))
    #         handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
    #         self.plot_handles[function_str] = handle
    #         self.functions_list.append(function_str) 
    #     else:
            
    #         x_vals = np.linspace(x_range[0], x_range[1], num_points)

    #         # Create a namespace for the math functions
    #         namespace = {'x': x_vals}
    #         namespace.update(math.__dict__)
    #         namespace.update({'exp': np.exp, 'sin': np.sin, 
    #                         'cos': np.cos, 'tan': np.tan,
    #                         'log': np.log10, 'ln': np.log, 
    #                         'sqrt': np.sqrt}) # type: ignore

    #         # Evaluate the function for each x value
    #         try:
    #             y_vals = eval(function_str, namespace)
    #         except:
    #             messagebox.showerror(title="Error", message="Invalid function.")
    #             print("Invalid function.")
    #             return

    #     if function_str not in self.plot_handles:
    #         # Create the plot
    #         handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
    #         self.plot_handles[function_str] = handle
    #         self.functions_list.append(function_str) 
    #         print(self.plot_handles)
    #     else:
    #         pass
        

   
    #     self.ax.set_xlim(xmin=x_min, xmax=x_max)  
    #     self.ax.set_ylim(ymin=y_min, ymax=y_max)
    #     self.ax.spines["left"].set_position("zero") #type:ignore
    #     self.ax.spines["bottom"].set_position("zero") #type:ignore
    #     self.ax.spines["right"].set_visible(False) #type:ignore
    #     self.ax.spines["top"].set_visible(False) #type:ignore

    #     self.ax.legend()    
    #     # Show the plot
    #     plt.show()

"""
This is confusing basically
"""


#  def plot_function(self):
#         # Get function string and x range from entry boxes
#         function_str = self.function_entry.get()

#         if self.x_min_entry.get() and self.x_max_entry.get():
#             try:
#                 x_min = float(self.x_min_entry.get())
#                 x_max = float(self.x_max_entry.get())
#             except ValueError:
#                 messagebox.showerror(title="Error", message="Invalid x range.")
#                 return
#         else:
#             messagebox.showerror(title="Error", message="Please enter x range.")
#             return

#         y_min = float(self.y_min_entry.get())
#         y_max = float(self.y_max_entry.get())

#         clr = str(self.color_entry.get())

#         num_points = 1000

#         # Check if the function has already been plotted
#         if function_str in self.plot_handles:
#             # Update the color of the existing plot
#             handle = self.plot_handles[function_str]
#             handle.set_color(clr)
#             messagebox.showwarning(title="Warning", message="The function already exists, ")
#         elif self.is_constant_function(function_str) is not None:
#             x_vals = np.linspace(x_min, x_max, 2)
#             y_vals = np.full(2, self.is_constant_function(function_str))
#             handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
#             self.plot_handles[function_str] = handle
#             self.functions_list.append(function_str) 
#         else:
#             x_vals = np.linspace(x_min, x_max, num_points)

#             # Create a namespace for the math functions
#             namespace = {'x': x_vals}
#             namespace.update(math.__dict__)
#             namespace.update({'exp': np.exp, 'sin': np.sin, 
#                             'cos': np.cos, 'tan': np.tan,
#                             'log': np.log10, 'ln': np.log, 
#                             'sqrt': np.sqrt}) # type: ignore

#             # Evaluate the function for each x value
#             try:
#                 y_vals = eval(function_str, namespace)
#             except:
#                 messagebox.showerror(title="Error", message="Invalid function.")
#                 print("Invalid function.")
#                 return

#             if function_str not in self.plot_handles:
#                 # Create the plot
#                 handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
#                 self.plot_handles[function_str] = handle
#                 self.functions_list.append(function_str) 
#             else:
#                 pass

#         self.ax.set_xlim(x_min, x_max)  
#         self.ax.set_ylim(y_min, y_max)
#         self.ax.spines["left"].set_position("zero") #type:ignore
#         self.ax.spines["bottom"].set_position("zero") #type: ignore 
#         self.ax.spines["right"].set_visible(False) #type:ignore
#         self.ax.spines["top"].set_visible(False) #type:ignore 
#         self.master.after(100, self.master.update)  # force update the window to show the plot
#         self.ax.legend()
#         plt.show()

# import matplotlib.pyplot as plt

# # Generate some sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# # Plot the data and get a reference to the line plot object
# line, = plt.plot(x, y)

# # Get the current x-data for the line plot
# current_xdata = line.get_xdata()

# # Update the x-min value
# new_xmin = 0
# new_xdata = [new_xmin] + current_xdata[1:]

# # Set the new x-data for the line plot
# line.set_xdata(new_xdata)

# # Update the plot to show the changes
# plt.show()

"""
Possible adjust
"""

# class PlotApp:
#     def __init__(self, master):
#         self.master = master
#         self.plot = Figure(figsize=(6, 4), dpi=100)
#         self.canvas = FigureCanvasTkAgg(self.plot, master=self.master)
#         self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, pady=10)

#         self.xmin_label = Label(self.master, text='xmin:')
#         self.xmin_label.grid(row=0, column=0, sticky=E, pady=5)
#         self.xmin_entry = Entry(self.master)
#         self.xmin_entry.grid(row=0, column=1, pady=5)

#         self.xmax_label = Label(self.master, text='xmax:')
#         self.xmax_label.grid(row=0, column=2, sticky=E, pady=5)
#         self.xmax_entry = Entry(self.master)
#         self.xmax_entry.grid(row=0, column=3, pady=5)

#         self.plot_button = Button(self.master, text='Plot', command=self.plot_handles)
#         self.plot_button.grid(row=2, column=0, pady=5)

#         self.clear_button = Button(self.master, text='Clear', command=self.clear_handles)
#         self.clear_button.grid(row=2, column=1, pady=5)

#         self.adjust_button = Button(self.master, text='Adjust', command=self.adjust_handles)
#         self.adjust_button.grid(row=2, column=2, pady=5)

#         self.quit_button = Button(self.master, text='Quit', command=self.master.quit)
#         self.quit_button.grid(row=2, column=3, pady=5)

#         self.handles = []
#         self.lines = []

#     def plot_handles(self):
#         x = np.linspace(-10, 10, 200)
#         y = np.sin(x)

#         handle_xvals = [float(h.get_x()) for h in self.handles]
#         handle_yvals = [float(h.get_y()) for h in self.handles]

#         for line in self.lines:
#             line.remove()
#         self.lines.clear()

#         for i in range(len(handle_xvals)):
#             line, = self.plot.plot(x + handle_xvals[i], y + handle_yvals[i], 'b-')
#             self.lines.append(line)

#         self.canvas.draw()

#     def clear_handles(self):
#         for handle in self.handles:
#             handle.remove()
#         self.handles.clear()

#         for line in self.lines:
#             line.remove()
#         self.lines.clear()

#         self.canvas.draw()

#     def adjust_handles(self):
#         xmin = float(self.xmin_entry.get())
#         xmax = float(self.xmax_entry.get())

#         for handle in self.handles:
#             x, y = handle.get_xy()
#             x_new = xmin + (x - self.xmin) * (xmax - xmin) / (self.xmax - self.xmin)
#             handle.set_x(x_new)

#         self.xmin = xmin
#         self.xmax = xmax

#         self.plot_handles()

#     def on_click(self, event):
#         if event.inaxes != self.plot.axes:
#             return

#         handle = self.plot.axvline(event.xdata, color='r')
#         self.handles.append(handle)

#         self.plot_handles()

#     def run(self):
#         self.plot_handles()
#         self.plot.canvas.mpl_connect('button_press_event', self.on_click)
#         self.master.mainloop()

#  x_vals = np.linspace(x_min, x_max, num_points)
#         # Create a namespace for the math functions
#         namespace = {'x': x_vals}
#         namespace.update(math.__dict__)
#         namespace.update({'exp': np.exp, 'sin': np.sin, 
#                         'cos': np.cos, 'tan': np.tan,
#                         'log': np.log10, 'ln': np.log, 
#                         'sqrt': np.sqrt,
#                         "arcsin": np.arcsin,
#                         "arccos": np.arccos,
#                         "arctan": np.arctan, }) # type: ignore

#         try:
#              y_vals = eval(function_str, namespace)
#         except:
#             messagebox.showerror(title="Error", message="Invalid function.")
#             print("Invalid function.")
#             return


#         for element in self.functions_list:
#             if element in self.plot_handles:
#                 handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
#                 self.plot_handles[element] = handle

#                 handle, = self.ax.plot(x_vals, y_vals, label=function_str, color=clr)
#                 self.plot_handles[function_str] = handle
#                 self.functions_list.append(function_str)

# import matplotlib.pyplot as plt

# # Plot some data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# plt.plot(x, y)

# # Clear the plot

# plt.pause(1)
# plt.clf()

# # Plot some other data
# x2 = [1, 2, 3, 4, 5]
# y2 = [1, 3, 5, 7, 9]
# plt.plot(x2, y2)

# # Show the plot
# plt.show()

#   if self.check_change(input=x_min, value=self.x_min) == False:
#               x_min = self.x_min[-1]
#             else:
#               pass

#             if self.check_change(input=x_max, value=self.x_max) == False:
#               x_max = self.x_max[-1]
#             else:
#               pass
            
#             if self.check_change(input=y_min, value=self.y_min) == False:
#               y_min = self.y_min[-1]
#             else:
#                 pass
#             if self.check_change(input=y_max, value=self.y_max) == False:
#               y_max = self.y_max[-1]
#             else:
#                 pass
            
#   def check_change(self, input, value):
#       if input == value:
#           return False
#       else:
#           return True

# self.x_min.clear()
# self.x_max.clear()
# self.y_max.clear()
# self.y_max.clear()

# self.x_min.append(x_min)
# self.x_max.append(x_max)

# self.y_min.append(y_min)
# self.y_max.append(y_max)

   # # current window values
        # self.x_min = []
        # self.y_min = []
        # self.x_max = []
        # self.y_max = []

# import matplotlib.pyplot as plt

# # Plot some data
# x = [1, 2, 3, 4, 5]
# y1 = [2, 4, 6, 8, 10]
# y2 = [1, 3, 5, 7, 9]
# plt.plot(x, y1, label='Graph 1')
# plt.plot(x, y2, label='Graph 2')

# # Clear all lines
# plt.pause(2)
# plt.clf()

# # Show the plot
# plt.show()

# my_dict = {'a': 1, 'b': 2, 'c': 3}

# # Iterate through every key in the dictionary
# for key in my_dict.keys():
#     print(key)

 # def evaluate_expression(self, expr):
    #     try:
    #         return eval(expr)
    #     except:
    #         return None
    
  
          
    # def is_constant_function(self, function_str):
    #     try:
    #         namespace = {
    #             'pi': math.pi,
    #             'e': math.e,
    #             'exp': np.exp,
    #             'sin': np.sin,
    #             'cos': np.cos,
    #             'tan': np.tan,
    #             'log': np.log10,
    #             'ln': np.log,
    #             'sqrt': np.sqrt,
    #             "arcsin": np.arcsin,
    #             "arccos": np.arccos,
    #             "arctan": np.arctan, 
    #         }
    #         namespace.update(math.__dict__)
    #         c = self.evaluate_expression(expr=function_str.format(**namespace))
    #         if isinstance(c, (int, float)):
    #             return c
    #        else:
    #             return None
    #     except:
    #         return None

import math
import numpy as np

# def evaluate_expression(expression):
#     constants = {"e": math.e, "pi": math.pi}
#     try:
#         return float(expression)
#     except ValueError:
#         for constant in constants:
#             if expression == constant:
#                 return constants[constant]
#         try:
#             return float(eval(expression))
#         except (NameError, TypeError, SyntaxError):
#             return None

def evaluate_expression(expression):
    constants = {'e': math.e, 'pi': math.pi,
                'exp': np.exp,
                'sin': np.sin,
                'cos': np.cos,
                'tan': np.tan,
                'log': np.log10,
                'ln': np.log,
                'sqrt': np.sqrt,
                "arcsin": np.arcsin,
                "arccos": np.arccos,
                "arctan": np.arctan, }
    return eval(expression, constants)

print(evaluate_expression('2 + 3'))              
print(evaluate_expression('sin(pi/2)'))          
print(evaluate_expression('ln(e**3)'))           
print(type(evaluate_expression('sqrt(16) + pi/2')))

   # def evaluate_expression(self, expr):
    #     try:
    #         return eval(expr)
    #     except:
    #         return None
    

          
    # def is_constant_function(self, function_str):
    #     try:
    #         namespace = {
    #             'pi': math.pi,
    #             'e': math.e,
    #             'exp': np.exp,
    #             'sin': np.sin,
    #             'cos': np.cos,
    #             'tan': np.tan,
    #             'log': np.log10,
    #             'ln': np.log,
    #             'sqrt': np.sqrt,
    #             "arcsin": np.arcsin,
    #             "arccos": np.arccos,
    #             "arctan": np.arctan, 
    #         }
    #         namespace.update(math.__dict__)
    #         c = self.evaluate_expression(expr=function_str.format(**namespace))
    #         if isinstance(c, (int, float)):
    #             return c
    #         else:
    #             return None
    #     except:
    #         return None