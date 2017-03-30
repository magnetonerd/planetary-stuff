import methods
from math import *
from numpy import *

Re = 6380.0e3

value = range(0,100)

def factorial(n):
    prod = 1.0
    if(n == 0):
        return 1
    else:
        for i in range (1,n+1):
            prod = prod*i
        return prod

def pot_approx(z):
    prod = 1.0
    sum = 1.0
    for i in value:
        x =(-1)*z/Re
        prod = prod * x
        sum = sum + prod
    
    return sum

def int_approx(z):
    prod = 1.0
    sum = 1.0
    for i in value:
        x =(-1)*z/Re
        prod = prod * x
        sum = sum + prod/factorial(i)
        print factorial(i), "\n"
    return sum

z = 0.0

for i in range(0,5):
    z = 1.0*i
    print pot_approx(z),int_approx(z)
