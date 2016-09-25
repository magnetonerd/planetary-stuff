from visual import* #Library used in order to do visual effects
from random import random #Allows the use of the random number generator in python
import math #So that I can use the math.floor function to allow me to define the velocity ranges I want
from visual.graph import *

def density(y):
    g = 9.8 #acceleration due to gravity (m/s)
    m = 0.02897/(6.022E23) #average mass of molecule (kg)
    R = 8.314 #Gas constant
    N = 6.022E23 #Avagodro's number
    n = 1.0 #mole
    k = 1.381E-23 #Boltzmann's constant (J/K)
    T = 300 - (y/100.0) #Tempurature based on dry adiabatic lapse rate (K)
    P = (1E5)*math.exp(-m*g*y/(k*T)) #Bariometric Pressure (N/m^2)
    rho = P*m*N/(R*T) #air density kg/(m^3)
    #print P,T,rho
    return rho

#This function is the implimentation for the improved Euler's Method
def F(vx,vy,vz,t,m,A,rho,k):
    cd = 0.5 #Drag coefficient
    dt = 0.01 #time step
    t = t + dt #time
    v = sqrt(vx**2 + vy**2 + vz**2) #magnitude of velosity
    c = 0.5*cd*rho*pi*A #Air Drag constant
    Fx = -c*vx*v
    Fy = -m*9.8 - c*v*vy
    Fz = -c*vz*v
    #The statements that follow are done so that I only had to write one function instead of three
    if(k == 1):
        return Fx     
    if(k == 2):
        return Fy
    if(k == 3):
        return Fz

func = gcurve(color = color.red)

y = 0.0
t = 0.0
dy = 1.0
dt = 0.01
rad = 0.037
A = pi*rad**2

values = range(0,15000)

for i in values:
    y = y + dy
    t = t + dt
    rho = density(y)
    Fx = F(100,-100,0,t,0.145,A,rho,1)
    Fy = F(100,-100,0,t,0.145,A,rho,2)
    Fz = F(100,-100,0,t,0.145,A,rho,3)
    Force = sqrt(Fx**2 + Fy**2 + Fz**2)
    #print y, Force
    func.plot(pos = (y, Force))
    
