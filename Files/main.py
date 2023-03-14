import matplotlib.pyplot as mpl
import time
import numpy
import scipy 

class math_function:
 pass

def plot_linear_function(a, b, clr, min_range, max_range):
 #y=ax+b

  x = list(range(min_range, max_range+1))
  y = [(a*i + b) for i in x]
  mpl.plot(x, y, label="linear", linestyle="-", color=clr)

plot_linear_function(1, 2, "r", -10, 10)

 