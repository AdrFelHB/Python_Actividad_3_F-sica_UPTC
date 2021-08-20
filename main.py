"""
Subject:    Introducción a la física computacional en python
Nombre:     Ejercicios 2.4, 2.5, 2.6
Autores:    Adrián Felipe Hernández Borda
            Eider David Torres Mesa cod 201811831
            Daniel Felipe Angarita Abril
"""

# load numpy module and pyplot from matplotlib library
import numpy as np
from matplotlib import pyplot as plt

#import all functions and variables from the package math
from math import * 

"""
Exercise:   2.4
Purpose:    Compute the time interval respect to earth and respect to a spaceship
            required by a spaceship that travels with velocity v from earth to any
            distant planet x lightyears away
Statement
            spaceship travels from Earth in a straight line at relativistic speed v to
            another planet x light years away. Write a program to ask the user for the value of x
            and the speed v as a fraction of the speed of light c, then print out the time in years that
            the spaceship takes to reach its destination (a) in the rest frame of an observer on Earth
            and (b) as perceived by a passenger on board the ship. Use your program to calculate
            the answers for a planet 10 light years away with v 0.99c.
"""


#   define function to find time in earth or spacecraft frame for any especific value of v in 

def compute_time(x,v):
    
    global t_spaceship, t_earth
    
    # ask user to chose between earth and spaceship reference frame
    
    frame_menu = True
    
    while frame_menu:
        print("Select the reference frame\n (1) Earth\n (2) Spaceship")
        selection = int(input())

        #   compute time for both of reference frames
        
        t_earth = np.abs(x/v)
        t_spaceship = np.abs(x / v) * np.sqrt(1 - (v**2))
        
        if selection == 1:
            t = t_earth
            frame_menu = False
        elif selection == 2:
            t = t_spaceship
            frame_menu = False
        else:
            pass
        
    #   print out the time in the selected frame
    
    print(f'the time measured in chosen reference frame is:\nt = {t:1.2f} years')

# define function to plot t in spaceship reference frame

def plot_time(x,v_s,t_rest,t_moving):
    
    #   using numpy define de domain set for velocities
    #   linspace function returns a vector with equally spaced numbers between an interval
    
    v = np.linspace(0.001,0.999,200)
    
    #   create a range set using time equations
    
    t_s = np.abs(x / v) * np.sqrt(1 - (v**2))
    t_e = np.abs(x/v)
    
    #   Create a pyplot figure for plotting
    
    fig = plt.figure()
    #   two subfigures are shown in a two columns arrange
    
    #   create a subplot in fig for plotting time interval in spacecraft depending on its velocity
    #   first subplot, right column
    
    ax1 = fig.add_subplot(1,2,1)
    #   title
    ax1.set_title(f'Time for traveling to {x:1.2f} light\nyears away planet measured in spaceship.')
    #   x and y labels
    ax1.set(xlabel=r'$\beta=\frac{v}{c}$',ylabel=r'$\Delta t$ in spaceship   [years]')
    #   limits for x and y axis
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, t_moving*1e1)
    
    #   Show a grid 
    ax1.grid(True)
    #   
    ax1.plot(v, t_s,'k-')
    ax1.plot([v_s],[t_moving],'or',label=r'$\Delta t_{s} = $' + str(round(t_moving,2)) + r'y for $v = $' + str(round(v_s,2)) + 'c')
    plt.legend()
    
    #   create a subplot in fig for plotting time interval in earth depending on ship velocity
    #   second subplot, right column
    
    ax2 = fig.add_subplot(1,2,2)
    #   title
    ax2.set_title(f'Time for traveling to {x:1.2f} light\nyears away planet measured on earth.')
    #   x and y labels
    ax2.set(xlabel=r'$\beta=\frac{v}{c}$',ylabel=r'$\Delta t$ in earth   [years]')
    #   limits for x and y axis
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, t_rest*1e1)
    #   Show a grid 
    ax2.grid(True)
    
    ax2.plot(v,t_e,'k-')
    ax2.plot([v_s],[t_rest],'ob',label=r'$\Delta t_{e} = $' + str(round(t_rest,2)) + r'y for $v = $' + str(round(v_s,2)) + 'c')
    plt.legend()
    # show legends and plots
    
    
    plt.show()    

#   main program

#   short exlpanation about what this program does

print("This program allows you to find the time dilatation for a spaceship that travels with speed 'v' a fraction of speed of light")

#   enter x and v as floating point variables

x = float(input("Enter the distance 'x' in light year \nx = "))
v = float(input("Enter the fraction of speed of light 'v', between (0,1)\nv = "))

#   next line guarantees that user has to enter a number between (0,1) for speed v

while np.abs(v) >= 1:
    v = float(input("Enter the fraction of speed of light 'v', between (0,1)\nv = "))

#   call functions to main program

compute_time(x,v)
plot_time(x,v,t_earth,t_spaceship)


"""
Exercise 2.5 Quantum potential step: Suppose we have a particle with mass equal to the electron mass m = 9.11 ×
10−31 kg and energy 10 eV encountering a potential step of height 9 eV. Write a Python
program to compute and print out the transmission and reflection probabilities using the formulas above.
"""


#Defining variables
m=float(input("Enter the mass of the particle in MeV/c^2: ")) #Asks the user for the value of the mass in MeV/c^2 units
E=float(input("Enter the initial kinetic energy E of the particle in eV: ")) #Asks the user for the value of the initial kinetic energy in eV units
V=float(input("Enter the potential energy V in eV: ")) #Asks the user for the value of the step potential in eV units
#Define a conditional
if E<V:
 print("The potential V is greater than the initial energy E and, therefore, the particle never will pass the step")#Print this message if E<V is satisfied (true)
else: #Execute the next codelines if the previous condition is false
 h=6.582119569*(10**-16) #Define a variable with the constant h-bar
 k1=(sqrt(2*m*(10**-6)*E))/h #Define an operation in order to calculate k1 using the values introduced by the user
 k2=(sqrt(2*m*(10**-6)*(E-V)))/h ##Define an operation in order to calculate k2 using the values introduced by the user
 T=(4*k1*k2)/((k1+k2)**2) #Define an operation for calculating transmission probability using k1 and k2
 R=((k1-k2)/(k1+k2))**2 #Define an operation for calculating reflection probability using k1 and k2
 print("The probability that the particle will be transmitted is about: ",round((T*100),2),"%") #Print the percent probability that particle will be transmitted
 print("The probability that the particle is reflected is about: ",round((R*100),2),"%") #Print the percent probability that particle will be reflected




"""
Exercise:   2.6
Statement:

            The orbit in space of one body around another, such as a planet around the Sun, need
            not be circular. In general it takes the formof an ellipse, with the body sometimes closer
            in and sometimes further out. If you are given the distance ℓ1 of closest approach that a
            planet makes to the Sun, also called its perihelion, and its linear velocity v1 at perihelion,
            then any other property of the orbit can be calculated from these two as follows.
               a) Kepler’s second law tells us that the distance ℓ2 and velocity v2 of the planet at
               its most distant point, or aphelion, satisfy ℓ2v2 = ℓ1v1. At the same time the total
               energy, kinetic plus gravitational, of a planet with velocity v and distance r from
               the Sun is given by...
   
for Earth
Lp:1.4710e11 #m
Vp:3.0287e4 #m/s
for halley
Lp:8.7830e10 #m
Vp:5.45290287e4 #m/s
"""

# We name the constants with which we are going to work.
# The constant of gravitation and the mass of the Sun.
G=6.6738E-11#N*m^2/kg^2
Ms=1.9891E30#kg
'' 'For the planet or orbiting body' ''

#we ask the user to enter the values of the distance and speed at perihelion
# LP = perihelion distance
# Vp = velocity at perihelion
Lp=float(input("Enter the distance to the Sun at perihelion:"))
Vp=float(input("Enter the value of velocity at perihelion:"))

'''
We look for the roots of our polynomial of degree two
Va = velocity at aphelion
Va**2-(2*G*Ms)/(Lp*Vp)Va-(Vp**2-2*G*(Ms/Lp)
comparing with ax ** 2 + bx + c we have that
'''
a=1
b=-(2*G*Ms)/(Lp*Vp)
c= -(2*G*Ms)/(Lp*Vp)
#then
pol_Va=[a, b,c]
#the function np.roots to find the reices of the polynomial
raices=np.roots(pol_Va)

'''
Since the value taken is the root that is different from the value entered
in velocity, since the aphelion velocity is different from that of perihelion 
for keppler's 2nd law we create a for loop for the arrangement of roots obtained 
and we condition to print the root that is different from the entered velocity 
value (perihelion) then,
'''

for i in raices:
  if (round(i,2)!=Vp ):
    Va=i
    print(f'v_2={Va*3.6} km/h')

#finally with the value of Va we find the length of the aphelion
La=(Vp*Lp)/Va
print(f'l_2={La*1000} km')

#PART B AND C
# WE DECLARE THE OPERATIONS GIVEN FOR THE EXERCISE
a=0.5*(Lp+La)
b=np.sqrt(Lp*La)
T=(2*np.pi*a*b)/(Lp*Vp)
e=(La-Lp)/(La+Lp)

#Finally, it remains for us to print the orbital period and the ecentricity of the orbits.
print(f'Orbital period {T*3.171e-8} years')
print(f'Eccentricity {e}')
