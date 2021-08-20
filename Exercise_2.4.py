"""
Subject:    Introducción a la física computacional en python
Nombre:     Ejercicios 2.4, 2.5, 2.6
Autores:    Adrián Felipe Hernández Borda
            Eider David Torres Mesa cod 201811831
            Daniel Felipe Angarita Abril
"""

"""
spaceship travels from Earth in a straight line at relativistic speed v to
another planet x light years away. Write a program to ask the user for the value of x
and the speed v as a fraction of the speed of light c, then print out the time in years that
the spaceship takes to reach its destination (a) in the rest frame of an observer on Earth
and (b) as perceived by a passenger on board the ship. Use your program to calculate
the answers for a planet 10 light years away with v 0.99c.
"""
"""
Exercise:   2.4
Purpose:    Compute the time interval respect to earth and respect to a spaceship
            required by a spaceship that travels with velocity v from earth to any
            distant planet x lightyears away
            
"""
# load numpy module and pyplot from matplotlib library
import numpy as np
from matplotlib import pyplot as plt



#   define function to find time in earth or spacecraft frame for any especific value of v

def compute_time(x,v):
    
    global t_spaceship, t_earth

        #   compute time for both of reference frames
        
    t_earth = np.abs(x/v)
    t_spaceship = np.abs(x / v) * np.sqrt(1 - (v**2))
    #   print out the time in the selected frame
    
    print(f'the time measured in earth reference frame is:\nt = {t_earth:1.2f} years')
    print(f'the time measured in spaceship reference frame is:\nt = {t_spaceship:1.2f} years')

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
    
    ax = fig.add_subplot(111)
    #   title
    ax.set_title(f'Time for traveling to {x:1.2f} light\nyears away planet.')
    #   x and y labels
    ax.set(xlabel=r'$\beta=\frac{v}{c}$',ylabel=r'$\Delta t$  [years]')
    #   limits for x and y axis
    ax.set_xlim(0, 1)
    ax.set_ylim(0, t_moving*1e2)
    
#    ax1.set_aspect('equal')
   #   Show a grid 
    ax.grid(True)
    #   
    ax.plot(v, t_s,'k-',label=r"$\Delta t' (v)$")
    ax.plot([v_s],[t_moving],'+k',label=r"$\Delta t' = $" + str(round(t_moving,2)) + r'y for $v = $' + str(round(v_s,2)) + 'c')
    ax.plot(v,t_e,'r-',label=r"$\Delta t (v)$")
    ax.plot([v_s],[t_rest],'+r',label=r"$\Delta t = $" + str(round(t_rest,2)) + r'y for $v = $' + str(round(v_s,2)) + 'c')
    plt.tight_layout()
    plt.legend()
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
