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
Failed attempt 
"""
#  def annote_plot(self):
#         fig, ax = plt.subplots()
#         ax.set_title("click on plot to annote")

#         def on_click(event):
#             if event.inaxes is not None:
#                 x, y = event.xdata, event.ydata
#                 ax.set_title(f"clicked at ({x:.2f}, {y:.2f}) ")
#         fig.canvas.mpl_connect('button_press_event', on_click)
#         plt.show()
