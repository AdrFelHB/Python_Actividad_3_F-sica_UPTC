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



#   define function to find time in earth or spacecraft frame for any especific value of v in 

def compute_time(x,v):
    
    global t_spaceship, t_earth
    
    # ask user to chose between earth and spaceship reference frame
    
    frame_menu = True
    
    while frame_menu:
        print("Select the reference frame\n (1) Earth\n (2) Spaceship\n (3) exit")
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
    ax1.set_title(f'Time for traveling to {x:1.2f} light years away planet\nmeasured in spaceship.')
    #   x and y labels
    ax1.set(xlabel=r'$\beta=\frac{v}{c}$',ylabel=r'$\Delta t$ in spaceship   [years]')
    #   limits for x axis
    ax1.set_xlim(0, 1)
    #   Show a grid 
    ax1.grid(True)
    #   
    ax1.plot(v, t_s,'k-')
    ax1.plot([v_s],[t_moving],'or',label=r'$\Delta t_{s} = $' + str(round(t_moving,2)) + r'y for $v = $' + str(round(v_s,2)) + 'c')
    
    #   create a subplot in fig for plotting time interval in earth depending on ship velocity
    #   second subplot, right column
    
    ax2 = fig.add_subplot(1,2,2)
    #   title
    ax2.set_title(f'Time for traveling to {x:1.2f} light years away planet\nmeasured on earth.')
    #   x and y labels
    ax2.set(xlabel=r'$\beta=\frac{v}{c}$',ylabel=r'$\Delta t$ in earth   [years]')
    #   limits for x axis
    ax2.set_xlim(0, 1)
    #   Show a grid 
    ax2.grid(True)
    
    ax2.plot(v,t_e,'k-')
    ax2.plot([v_s],[t_rest],'ob',label=r'$\Delta t_{e} = $' + str(round(t_rest)) + r'y for $v = $' + str(round(v_s,2)) + 'c')
    
    # show legends and plots
    
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
