from root_finding import *
from math import *

def f1 ( x ) :
    return tan(x)

def f2 ( x ) :
	return tanh(x)


print(" Algorithms for root of tan(x)")
print(" ------------------------------------------------")

print(" 1. Simple search")
x0 = float ( input(" Enter initial guess x_0 : ") )
dx = float ( input(" Enter step dx : ") )
acc = float ( input(" Enter accuracy : ") )
answer = root_simple(f1, x0, dx, acc,1000,True)
print  str ( answer ) + "\n\n"

print(" 2. Bisection search")
x0 = float ( input(" Enter bracketing guess x_0 : ") )
x1 = float ( input(" Enter bracketing guess x_1 : ") )
acc = float ( input(" Enter accuracy : ") )
answer = root_bisection(f1, x0, x1, acc,1000,True)
print  str ( answer ) + "\n\n"

print(" Algorithms for root of tanh(x)")
print(" ------------------------------------------------")

print(" 1. Simple search")
x0 = float ( input(" Enter initial guess x_0 : ") )
dx = float ( input(" Enter step dx : ") )
acc = float ( input(" Enter accuracy : ") )
answer = root_simple(f2, x0, dx, acc,1000,True)
print  str ( answer ) + "\n\n"

print(" 2. Bisection search")
x0 = float ( input(" Enter bracketing guess x_0 : ") )
x1 = float ( input(" Enter bracketing guess x_1 : ") )
acc = float ( input(" Enter accuracy : ") )
answer = root_bisection(f2, x0, x1, acc,1000,True)
print  str ( answer ) + "\n\n"


"""How to break the tangent root finder:"""
'''
print(" Please be gentle... ")
print(" Broken algorithm for root of tan(x)")
print(" ------------------------------------------------")

print(" 1. Simple search")
x0 = pi/2 
dx = pi/8
acc = 0.001
print("Requested values are: x0 = " + str(x0) +", dx = " + str(dx) + ", acc = " + str(acc) + ".")
answer = root_simple(f1, x0, dx, acc,1000,True)
print  str ( answer ) + "\n\n"
'''
