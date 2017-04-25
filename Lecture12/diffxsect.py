#Takes data, solves for differential cross section

from math import *
from numpy import array, diff
import matplotlib.pyplot as plt

#def dTheta_db(theta, step):

file = open('results4.txt', 'r')
lines = file.readlines()
x = []
y = []
for line in lines :
	if line != '\n' :
		words = line.split()
		ix, iy = [float(s) for s in words]
		x.append(ix)
		y.append(iy)
#for stuff in x,y:
#	print stuff
#^ for debugging

b = array( x )
theta = array( y )
xsection = [0]
#dtdb = dTheta_db(theta, 0.05)
#dtdb = []
db = 0.1
dt = diff(theta)/db
#dtdb.append(dt)

for i in xrange(len(dt)):
	xsval = abs((b[i]/sin(theta[i]))*(1/dt[i]))
	xsection.append(xsval)

plt.plot(b, xsection)
plt.xlabel('b')
plt.ylabel('Diff Cross-Sect.')
plt.show()