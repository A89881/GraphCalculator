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
