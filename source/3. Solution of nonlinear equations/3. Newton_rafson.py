import math

# System of equations
def f1(x, y):
    return math.sin(y + 1) - x - 1.2

def f2(x, y):
    return 2*y + math.cos(x) - 2

# Partial derivatives of the system functions
def difx1dx(x, y):
    return -1

def dify1dy(x, y):
    return math.cos(y+1)

def difx2dx(x, y):
    return math.sin(x)*(-1)

def dify2dy(x, y):
    return 2

# Vector function F(x, y)
def Fun(x, y):
    return [f1(x, y), f2(x, y)]

# Jacobian matrix
def Jacobian(x, y):
    return [[difx1dx(x, y), dify1dy(x, y)],
            [difx2dx(x, y), dify2dy(x, y)]]

# Newton-Raphson method for the system of equations
def newtonRaphson(x0, y0, eps):
    x, y = x0, y0
    Fx = Fun(x, y)
    i = 0
    while abs(Fx[0]) > eps or abs(Fx[1]) > eps:
        J = Jacobian(x, y)
        detJ = J[0][0]*J[1][1] - J[0][1]*J[1][0]
        if abs(detJ) < eps:
            raise ValueError("The Jacobian matrix is singular, no solutions exist.")
        dx = (J[1][1]*Fx[0] - J[0][1]*Fx[1]) / detJ
        dy = (J[0][0]*Fx[1] - J[1][0]*Fx[0]) / detJ
        x -= dx
        y -= dy
        Fx = Fun(x, y)
        i += 1
    return [x, y, i]


x0 = float(input("Enter initial approximation x0: "))
y0 = float(input("Enter initial approximation y0: "))
eps = float(input("Enter accuracy eps: "))

try:
    roots = newtonRaphson(x0, y0, eps)
    print("Found roots of the system of equations: x = {}, y = {}, Number of iterations = {}".format(roots[0], roots[1], roots[2]))
except ValueError as e:
    print("Error:", e)
