from grav_pot_approx import *
from gaussquad import gaussxwab

N = 100

G = 6.674e-11
Re = 6.371e6
M = 5.97e24

def integrand(z,t):

    return int_approx(z*t)*exp(-t)

t,w = gaussxwab(N,0.0,1000)

def pot_exact(z,t):
    sum = 0.0
    
    for i in range(0,N):
        sum = sum + integrand(z,t[i])*w[i]

    return sum*z*G*M/Re**2

def pot(z):
    return pot_exact(z,t)
