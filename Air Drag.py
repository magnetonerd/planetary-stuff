from visual import* #Library used in order to do visual effects
from random import random #Allows the use of the random number generator in python
import math #So that I can use the math.floor function to allow me to define the velocity ranges I want
from visual.graph import *

def density(y):
    g = 9.8
    m = 0.02897/(6.022E23)
    R = 8.314
    N = 6.022E23
    k = 1.381E-23
    T = 300 - (y/100.0)
    P = (1E5)*math.exp(-m*g*y/(k*T))
    rho = P*m/(N*k*T) #kg/(m^3)
    return rho

#This function is the implimentation for the improved Euler's Method
def F(vx,vy,vz,t,m,r,rho,k):
    cd = 0.1
    dt = 0.01
    t = t + dt
    v = sqrt(vx**2 + vy**2 + vz**2)
    c = 0.5*pi*cd*rho
    Fx = -c*vx*v
    Fy = -c*vy*v - m*9.8
    Fz = -c*vz*v
    #The statements that follow are done so that I only had to write one function instead of three
    if(k == 1):
        return Fx     
    if(k == 2):
        return Fy
    if(k == 3):
        return Fz

Ratom = 0.3

r = Ratom

#This function is used to define the random velocities of the projectile  
def rand_vel(a):
    #The lists that will store the random numbers that will be used for the velocities
    vals1 = [0]*3001 #vx and vz
    vals2 = [0]*1001 #vy
    values1 = range(0,2000)
    values2 = range(0,1000)
    if(a == 5):
        #Generates the numbers that will be used in the x and z velocities
        for i in values1:
            rand_var1 = 10*random()
            show_num1 = math.floor(rand_var1) + 5
            if((show_num1%2) == 1):
                vals1[i] = show_num1
            else:
                vals1[i] = -show_num1
            return vals1[i]
    if(a == 10):
        #Generates the numbers that will be used in the y velocity
        for i in values2:
            rand_var2 = 10*random()
            show_num2 = math.floor(rand_var2) + 10 #There are ranges for this that the sim doesn't like so the + 10 is used to ensure they aren't uesd
            vals2[i] = show_num2        
            return vals2[i]

func = gcurve(color = color.red)
    
#Gives 360 lighting to the set
light = local_light(pos=vector(0,40,0),color=color.gray(0.75))

hopeImright = open("Rodgers ball2.txt","w") #Opens a file to write data to

#Makes the headers of the write file.
hopeImright.write("Alttidue")
hopeImright.write(",")
hopeImright.write("Force")
hopeImright.write(",")
hopeImright.write("\n")

#this is the boundary that is used to make the ball fly over.
#length defines how far to the left and right the background will extend
#hihght is how much the background extends in the up and down direction
#width is how far backward and forward the background will extend.
#color defines the color of the background. Green in this case
background = box(length = 100,hight = 1,width = 100, color = color.green)

#It is a good idea to have our system setup so that quick changes can
#be made to the intial conditions of the position of the ball
bx = -5.0 #x-component
by = 1.0 #y-component
bz = -5.0 #z-component

#This is the ball that will be made to fly.
#pos initialzes the position of the ball on the screen.
#Raduis defines the radius of the ball in the units that the
#call function defines.
#The color of the ball is blue.
ball = sphere(pos = vector(bx,by,bz),radius = 5, color = color.red)

density_mist = 0.5

R_init = ball.radius

R = R_init

m_ball_init = 1.0

m_ball = m_ball_init

cube1 = box(pos=vector(5,1.5,-5),length=2,width=2,height=2,color=color.cyan)
cube2 = box(pos=vector(-5,1.5,5),length=2,width=2,height=2,color=color.cyan)

#So that I can have the initial y value saved for later use.
x_init = bx
y_init = by
z_init = bz

#The lists that will store the random numbers that will be used for the velocities
vals1 = [0]*31 #vx and vz
vals2 = [0]*11 #vy

#Ranges for the for loops that are used for velocities
values1 = range(0,20)
values2 = range(0,10)

#Generates the numbers that will be used in the x and z velocities
for i in values1:
    vals1[i] = rand_vel(5)

#Generates the numbers that will be used in the y velocity
for i in values2:
    vals2[i] = rand_vel(10)

values3 = range(0,1)

for i in values3:

    vx = 75.0#vals1[i]*10    #x-component of the velocity
    vy = -100.0#vals2[i]*10   #y-component of the velocity
    vz = 0.0#vals1[i+10]*10 #z-component of the velocity
    print "vx =",vx,"vy =",vy,"vz =",vz

    #saves the initial y velocity for future use.
    vx_init = vx
    vy_init = vy
    vz_init = vz

    ax = 2.0 #x-component of the acceleration
    ay = -9.8 #y-component of the acceleration
    az = 2.0 #z-component of the acceleration

    F0_mx = ax
    F0_my = ay
    F0_mz = az

    dt = 0.01 #Step size of the time variable
    t = 0.0 #Initialization of the time variable
    tg = 0.0
    
    #boolen variable to determine when the loop will close.
    state = True

    vel = sqrt(vx**2+vy**2+vz**2)

    #This loop insures that the ball will fly until the window is closed
    while (state == True):
        rate(100)#Refresh rate
        t = t + dt #The time at each iteration of the loop
        tg = tg + dt
        #The ball will not fly unless it is told to do so.
        #The if statement defines the velocity based on the
        #position of the ball.

        ball.radius = r

        #Here are the calls for the different components of the original force
        rho = density(by)
        F0x = F(vx,vy,vz,t,m_ball,ball.radius,rho,1)
        F0y = F(vx,vy,vz,t,m_ball,ball.radius,rho,2)
        F0z = F(vx,vy,vz,t,m_ball,ball.radius,rho,3)

        #These are the x,y,z components of the position
        #as defined by the partial kinematic equation:
        bxg = bx + vx*dt #new x-component guess of the ball position
        byg = by + vy*dt #new y-component guess of the ball position
        bzg = bz + vz*dt #new z-component guess of the ball position
        #x = x0 + v*t. The quadratic time term is left out
        #because even though it does simulate the lower
        #new hight, after enough iterations the ball
        #will just stop bouncing and start to just slowly
        #move downward.

        vxg = vx + F0_mx*dt #new x-component guess of the ball velocity
        vyg = vy + F0_my*dt #new x-component guess of the ball velocity
        vzg = vz + F0_mz*dt #new x-component guess of the ball velocity

        #Here are the calls for the guessed compenents of the force
        Fgx = F(vxg,vyg,vzg,t,m_ball,ball.radius,rho,1)
        Fgy = F(vxg,vyg,vzg,t,m_ball,ball.radius,rho,2)
        Fgz = F(vxg,vyg,vzg,t,m_ball,ball.radius,rho,3)        

        func.plot(pos = (bx,by))

        #The 1.0 is the mass of the function
        bx = bx + (vx + vxg)*dt/2.0
        by = by + (vy + vyg)*dt/2.0
        bz = bz + (vz + vzg)*dt/2.0
        vx = vx + (F0x + Fgx)*dt/(2.0)
        vy = vy + (F0y + Fgy)*dt/(2.0)
        vz = vz + (F0z + Fgz)*dt/(2.0)

        if(by < 1):
            #This will keep the ball moving in the same x direction
            #as it was when the ball first started moving.
            vx = vx
            #This sends the ball back up when it reaches the boundary
            #of the background.
            vy = -vy
            #This will keep the ball moving in the same z direction
            #as it was when the ball first started moving.
            vz = vz
        
        else:
            #If the acceleration term is not added into this statement
            #the ball will reach the background and then it will start
            #over at the beginning. So, the acceleration in the y
            #direction term insures that the ball will actually move
            #through a trajectory. Giving the ball the apperance of projectile.
            vx = vx + ax*dt #x-component of the velocity
            vy = vy + ay*dt #y-component of the velocity
            vz = vz + az*dt #z-component of the velocity
            #The x and z components of the velocity are inserted here
            #for the purpose of future expantion.

        #This is used to ensure an update of the position of the ball.
        ball.x = bx #Positions to the left and right of center screen
        ball.y = by #Positions above and below the center of the screen
        ball.z = bz #Positions behind and in front of the center of the screen

        #In order to keep the ball on the background it is set to its
        #initial conditions. This makes the ball follow a projectile
        #path, and then it restart from the beginning.
        if (abs(bx) > 1000.0 or abs(bz) > 1000.0):
            bx = x_init
            by = y_init
            bz = z_init
            vx = vx_init
            vy = vy_init
            vz = vz_init
            #This boolean condition closes out the while loop
            #it ensures that only one arc is gone through.
            state = False
                
        #This writes to the file defined from above in the open statement
        hopeImright.write(str(Fgy))
        hopeImright.write(",")
        hopeImright.write(str(by))
        hopeImright.write(",")
        hopeImright.write("\n")

hopeImright.close() #Closes the write file
