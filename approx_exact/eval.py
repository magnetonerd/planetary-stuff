from grav_pot_approx import *
from grav_pot_exact import *

z = 0.0

for i in range(0,10):
    z += 1.0*i
    
    print pot(z)
