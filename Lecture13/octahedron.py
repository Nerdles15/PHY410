from cpt import *

print " Resistor octahedron equations"
print " -----------------------------"

v0 = 1
r1 = 1
r2 = r1
r3 = r1
r4 = r1
r5 = r1
r6 = r1
r7 = r1
r8 = r1
r9 = r1
r10 = r1
r11 = r1
r12 = r1

v = Matrix(5, 1)       # column vector with 5 rows
v[0][0] = v0
print 'v = '
print v 

#matrix below follows equivalent resistance at R[i+2][j+2] node
# since nodes 1, 8 are the terminals of the voltage supply
#this is applicable to any two nodes being the terminals
# so it is completely general

R = Matrix(5, 5)            # 5x5 resistance matrix
R[0][0] = r9 + r10 + r11 + r12 # equivalent resistance at node 2
R[0][1] = -r9               # resistance between nodes 2, 3
R[0][2] = -r10              # resistance between nodes 2, 4
R[0][3] = -r11              # resistance between nodes 2, 5
R[0][4] = -r12              # resistance between nodes 2, 6

R[1][0] = -r9               # equivalent resistance at node 3
R[1][1] = r1 + r5 + r6 + r9
R[1][2] = -r6
R[1][3] = 0
R[1][4] = -r5

R[2][0] = -r10              # equivalent resistance at node 4
R[2][1] = -r6
R[2][2] = r2 + r6 + r7 + r10
R[2][3] = -r7
R[2][4] = 0

R[3][0] = -r11              # equivalent resistance at node 5
R[3][1] = 0
R[3][2] = -r7
R[3][3] = r3 + r7 + r8 + r11
R[3][4] = -r8

R[4][0] = -r12              # equivalent resistance at node 6
R[4][1] = -r5
R[4][2] = 0
R[4][3] = -r8
R[4][4] = r4 + r5 + r8 + r12

print 'R = '
print R

# the solve_Gauss_Jordan replaces R by R^-1 and v by i
# so save the original R and copy v into a vector i
R_save = Matrix_copy(R)
i = Matrix_copy(v)

solve_Gauss_Jordan(R, i)
print " \nSolution using Gauss-Jordan elimination"
print " i(1) = " + str(i[0])
print " i(2) = " + str(i[1])
print " i(3) = " + str(i[2])
print " i(4) = " + str(i[3])
print " i(5) = " + str(i[4])

# see whether LU decomposition gives the same answer
i = Vector(v)
solve_LU_decompose(R_save, i)
print " \nSolution using LU Decompositon"
print " i(1) = " + str(i[0])
print " i(2) = " + str(i[1])
print " i(3) = " + str(i[2])
print " i(4) = " + str(i[3])
print " i(5) = " + str(i[4])

iT = 0.
print " \nTotal current running through model: "
i1 = float(i[0][0])
i2 = float(i[1][0])
i3 = float(i[2][0])
i4 = float(i[3][0])
i5 = float(i[4][0])
iT += i1 + i2 + i3 + i4 + i5
print iT
print " \nEffective Resistance (is futile...): "
reff = v0/iT
print reff

