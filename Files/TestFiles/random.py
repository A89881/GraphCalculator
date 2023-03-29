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

# Function for Integral 
# def plot_function(self):
#       # Get function string and x range from entry boxes
#       function_str = self.function_entry.get()
#       x_min = float(self.x_min_entry.get())
#       x_max = float(self.x_max_entry.get())
#       x_range = (x_min, x_max)
#       clr = str(self.color_entry.get())

#       # Check if the function has already been plotted
#       if function_str in self.plot_handles:
#           # Update the color of the existing plot
#           handle = self.plot_handles[function_str]
#           handle.set_color(clr)
#           messagebox.showwarning(title="Warning", message="The function already exists")
#       else:
#           num_points = abs(int(x_range[0])) + abs(int(x_range[1]))
#           # Define the x values to plot
#           if num_points < 1000:
#               num_points = 1000
#           else:
#               num_points = abs(int(x_range[0])) + abs(int(x_range[1]))
#           x_vals = np.linspace(x_range[0], x_range[1], num_points)

#           # Create a namespace for the math functions
#           namespace = {'x': x_vals}
#           namespace.update(math.__dict__)
#           namespace.update({'exp': np.exp, 'sin': np.sin, 
#                             'cos': np.cos, 'tan': np.tan,
#                             'log': np.log10, 'ln': np.log, 
#                             'sqrt': np.sqrt}) # type: ignore

#           # Evaluate the function for each x value
#           try:
#               y_vals = eval(function_str, namespace)
#           except:
#               messagebox.showerror(title="Error", message="Invalid function.")
#               print("Invalid function.")
#               return

#           # Create the plot
#           if all(y_vals < 0):
#               plt.fill_between(x_vals, y_vals, 0, where=y_vals<0, label=function_str, color=clr)
#           elif all(y_vals > 0):
#               plt.fill_between(x_vals, y_vals, 0, where=y_vals>0, label=function_str, color=clr)
#           else:
#               plt.fill_between(x_vals, y_vals, 0, where=y_vals>0, label=function_str, color=clr)
#               plt.fill_between(x_vals, y_vals, 0, where=y_vals<0, color=clr)

#           self.plot_handles[function_str] = True

#           # Add labels and title
#           plt.xlabel("X-Axis")
#           plt.ylabel("Y-Axis")
#           plt.legend()

#           # Show the plot
#           plt.show()

# import flet as ft

# def main(page: ft.Page):
#     page.title = "Flet counter example"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

#     def minus_click(e):
#         txt_number.value = str(int(txt_number.value) - 1)
#         page.update()

#     def plus_click(e):
#         txt_number.value = str(int(txt_number.value) + 1)
#         page.update()

#     page.add(
#         ft.Row(
#             [
#                 ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
#                 txt_number,
#                 ft.IconButton(ft.icons.ADD, on_click=plus_click),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#         )
#     )

# ft.app(target=main)