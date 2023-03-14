# import tkinter as tk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure

# # Define the Matplotlib graphing function
# def create_graph(x, y):
#     fig = Figure(figsize=(5, 4), dpi=100)
#     ax = fig.add_subplot(111)
#     ax.plot(x, y)
#     return fig

# # Define the UI
# class GraphingCalculator(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.master.title("Graphing Calculator")
        
#         # Add UI elements
#         self.x_label = tk.Label(self.master, text="X values:")
#         self.x_entry = tk.Entry(self.master)
#         self.y_label = tk.Label(self.master, text="Y values:")
#         self.y_entry = tk.Entry(self.master)
#         self.plot_button = tk.Button(self.master, text="Plot", command=self.plot_graph)
#         self.canvas = FigureCanvasTkAgg(create_graph([], []), master=self.master)
        
#         # Layout UI elements
#         self.x_label.pack()
#         self.x_entry.pack()
#         self.y_label.pack()
#         self.y_entry.pack()
#         self.plot_button.pack()
#         self.canvas.get_tk_widget().pack()
        
#     # Define the function to update the graph
#     def plot_graph(self):
#         x = [float(i) for i in self.x_entry.get().split()]
#         y = [float(i) for i in self.y_entry.get().split()]
#         self.canvas.get_tk_widget().destroy()
#         self.canvas = FigureCanvasTkAgg(create_graph(x, y), master=self.master)
#         self.canvas.get_tk_widget().pack()

# # Create and run the UI
# root = tk.Tk()
# app = GraphingCalculator(master=root)
# app.mainloop()

# class GraphingCalculator:
#     def __init__(self, master):
#         self.master = master
#         master.title("Graphing Calculator")

#         # Create input widgets for the range of x values
#         self.x_range_frame = tk.Frame(master)
#         self.x_range_frame.pack(side=tk.TOP, padx=10, pady=5)

#         self.x_range_label = tk.Label(self.x_range_frame, text="X Range:")
#         self.x_range_label.pack(side=tk.LEFT)

#         self.x_min_entry = tk.Entry(self.x_range_frame, width=6)
#         self.x_min_entry.pack(side=tk.LEFT)

#         self.to_label = tk.Label(self.x_range_frame, text="to")
#         self.to_label.pack(side=tk.LEFT)

#         self.x_max_entry = tk.Entry(self.x_range_frame, width=6)
#         self.x_max_entry.pack(side=tk.LEFT)

#         # Create input widgets for the function to graph
#         self.function_frame = tk.Frame(master)
#         self.function_frame.pack(side=tk.TOP, padx=10, pady=5)

#         self.function_label = tk.Label(self.function_frame, text="Function:")
#         self.function_label.pack(side=tk.LEFT)

#         self.function_entry = tk.Entry(self.function_frame, width=30)
#         self.function_entry.pack(side=tk.LEFT)

#         # Create button to plot the function
#         self.plot_button = tk.Button(master, text="Plot", command=self.plot_function)
#         self.plot_button.pack(side=tk.TOP, padx=10, pady=5)
        
#     def plot_function(self):
#         # Get the range of x values from the input widgets
#         try:
#             x_min = float(self.x_min_entry.get())
#             x_max = float(self.x_max_entry.get())
#         except ValueError:
#             tk.messagebox.showerror("Error", "Invalid input for x range.")
#             return

#         # Get the function to plot from the input widget
#         function_str = self.function_entry.get()

#         # Plot the function using the plot_math_function function
#         try:
#             plot_math_function(function_str, x_range=(x_min, x_max))
#         except:
#             tk.messagebox.showerror("Error", "Invalid function.")
