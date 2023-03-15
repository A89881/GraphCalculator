from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import math
import tkinter as tk

class GraphingCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Graphing Calculator")
        self.plot_handles = {}  # keep track of plotted functions and their colors

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

        # Create color input label and entry box
        self.color_label = tk.Label(master, text="color: ")
        self.color_label.pack()
        self.color_entry = tk.Entry(master)
        self.color_entry.pack()

        # Create plot button
        self.plot_button = tk.Button(master, text="plot", command=self.plot_function)
        self.plot_button.pack()

    def plot_function(self):
        # Get function string and x range from entry boxes
        function_str = self.function_entry.get()
        x_min = float(self.x_min_entry.get())
        x_max = float(self.x_max_entry.get())
        x_range = (x_min, x_max)
        clr = str(self.color_entry.get())

        # Check if the function has already been plotted
        if function_str in self.plot_handles:
            # Update the color of the existing plot
            handle = self.plot_handles[function_str]
            handle.set_color(clr)
            messagebox.showwarning(title="Warning", message="The function already exists")
        else:
            num_points = abs(int(x_range[0])) + abs(int(x_range[1]))
            # Define the x values to plot
            if num_points < 1000:
                num_points = 1000
            else:
                num_points = abs(int(x_range[0])) + abs(int(x_range[1]))
            self.x_vals = np.linspace(x_range[0], x_range[1], num_points)

            # Create a namespace for the math functions
            namespace = {'x': self.x_vals}
            namespace.update(math.__dict__)
            namespace.update({'exp': np.exp, 'sin': np.sin, 
                              'cos': np.cos, 'tan': np.tan,
                              'log': np.log10, 'ln': np.log, 
                              'sqrt': np.sqrt}) # type: ignore

            # Evaluate the function for each x value
            try:
                self.y_vals = eval(function_str, namespace)
            except:
                messagebox.showerror(title="Error", message="Invalid function.")
                print("Invalid function.")
                return

            # Create the plot
            handle, = plt.plot(self.x_vals, self.y_vals, label=function_str, color=clr)
            self.plot_handles[function_str] = handle
        
        # Add labels and title
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.legend()
        plt.show()
 

#     def find_nearest_index(array, value):
#         return np.abs(array - value).argmin()

#     def on_hover(event):
#         if event.inaxes is not None and event.inaxes.get_lines():
#             line = event.inaxes.get_lines()[0]
#             xdata = line.get_xdata()
#             ydata = line.get_ydata()
#             x, y = event.xdata, event.ydata
#             index = find_nearest_index(xdata, x)
#             x_val, y_val = xdata[index], ydata[index]
#             plt.title(f"({x_val:.2f}, {y_val:.2f})")
#             plt.draw()

#     def on_press(event):
#         if event.inaxes is not None and event.inaxes.get_lines():
#             line = event.inaxes.get_lines()[0]
#             xdata = line.get_xdata()
#             ydata = line.get_ydata()
#             x, y = event.xdata, event.ydata
#             index = find_nearest_index(xdata, x)
#             x_val, y_val = xdata[index], ydata[index]
#             plt.title(f"({x_val:.2f}, {y_val:.2f})")
#             plt.draw()
#             fig.canvas.mpl_disconnect(hover_cid)
#             fig.canvas.mpl_connect('motion_notify_event', on_move)

#     def on_move(event):
#         if event.inaxes is not None and event.inaxes.get_lines():
#             line = event.inaxes.get_lines()[0]
#             xdata = line.get_xdata()
#             ydata = line.get_ydata()
#             x, y = event.xdata, event.ydata
#             index = find_nearest_index(xdata, x)
#             x_val, y_val = xdata[index], ydata[index]
#             plt.title(f"({x_val:.2f}, {y_val:.2f})")
#             plt.draw()

#     def plot_functions(functions):
#         fig, ax = plt.subplots()
#         handle = None
#         for function_str, color in functions:
#             x = np.linspace(-5, 5, 1000)
#             y = eval(function_str)
#             handle, = ax.plot(x, y, color=color, label=function_str)
#         ax.legend()
#         ax.set_xlabel('X')
#         ax.set_ylabel('Y')
#         ax.set_title('Hover over plot to see coordinates')
#         hover_cid = fig.canvas.mpl_connect('motion_notify_event', on_hover)
#         press_cid = fig.canvas.mpl_connect('button_press_event', on_press)
#         fig.canvas.mpl_connect('key_press_event', lambda event: toggle_functions(event, ax, functions))
#         plt.show()

#     def toggle_functions(event, ax, functions):
#         if event.key == 'escape':
#             plt.close()
#         elif event.key.isdigit() and int(event.key) < len(functions):
#             function_str, color = functions[int(event.key)]
#             x = np.linspace(-5, 5, 1000)
#             y = eval(function_str)
#             handle, = ax.plot(x, y, color=color, label=function_str)
#             ax.legend()
#             plt.draw()

# functions = [
#     ('np.sin(x)', 'blue'),
#     ('np.cos(x)', 'red'),
#     ('np.tan(x)', 'green'),
#     ('np.exp(-x**2)', 'purple')
# ]
# plot_functions(functions)
   
plt.grid()
root = tk.Tk()
graphing_calculator = GraphingCalculator(root)
root.mainloop()
