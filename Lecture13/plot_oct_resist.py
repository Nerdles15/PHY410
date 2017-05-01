from math import *
from numpy import array, diff
import matplotlib.pyplot as plt

#file configuration is: column 1 = individual resistor value
# column 2 = iT (total current) value
# column 3 = r effective (effective resistance) value
file = open('oct_resistance.txt', 'r')
lines = file.readlines()
x = []
y = []
for line in lines:
	if line != '\n' :
		words = line.split()
		ix, iy = [float(s) for s in words]
		x.append(ix)
		y.append(iy)

plt.plot(x, y)
plt.xlabel('Individual Resistor Resistance (Ohms)')
plt.ylabel('Equivalent Resistance')
plt.show()