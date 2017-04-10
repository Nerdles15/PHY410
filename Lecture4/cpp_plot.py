from read_plot import *

[x,y] = read_plot("histogram.dat")
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.xlabel('Magnitude (M)')
plt.ylabel('log(N)')
plt.show()