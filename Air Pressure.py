from visual import *
from math import *

#Coder: Christopher Rodgers
#Class: PHYS 420
#Name: Exponential Atmosphere 1.16 (d)
#Explanasion: This is a simple program to do calculations
#on the pressure in the atmosphere at four different locations
#in the world. It uses the exact solution to the problem,
#because there are only four heights to calculate the pressure.

P0 = 1.0 #initial pressure

m = 0.02897/(6.022e23) #average mass of air molecules in kg

g = 9.8 #acceleration due to gravity (m/s)

k = 1.381e-23 #boltzman's constant (J/K)

T = 293.0 #temperature (K)

P = [0]*4 #Calculating four pressures

z = [0]*4 #Pressures are at 4 different hights in meters

z[0] = 1430 #Ogden, Utah

z[1] = 3090 #Leadville, Colorado

z[2] = 4420 #Mt. Whitney, California

z[3] = 8850 #Mt. Everest, Nepal

b = [0]*4 #help simplify calculations later

val = range(4)

#z = 0.0

for i in val:
    #exponent for each hight
    b[i] = -m*g*z[i]/(k*T)
    #Calculation of pressure for each exponent
    P[i] = P0*math.exp(b[i])
    print P[i]
    
#The pressure at Ogdan is 0.8465
#The pressure at Leadville is 0.6977
#The pressure at Mt. Whitney is 0.5975
#The pressure at Everest is 0.3566
