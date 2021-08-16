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


# enter x and v as floating point variables
def single_speed_value():
    x = float(input("Enter the distance 'x' in light year \nx = "))
    v = float(input("Enter the fraction of speed of light 'v', between (0,1)\nv = "))
    while v >= 1:
        v = float(input("Enter the fraction of speed of light 'v', between (0,1)\nv = "))

    # ask user to chose between earth and spaceship reference frame
    option = True
    while option:
        print("Select the reference frame\n (1) Earth\n (2) Spaceship")
        selection = int(input())
        if selection == 1:
            option = False
            t = np.abs(x/v)
        elif selection == 2:
            option = False
            t = np.abs(x / v) * np.sqrt(1 - (v**2))
        else:
            pass
    print(f'the time measured in chosen reference frame is:\nt = {t:1.3f} years')

def several_speed_values():
    v = np.linspace(0.001,0.999,100)
    x = float(input('Enter the distance \'x\' in light year \nx = '))
    t = np.abs(x / v) * np.sqrt(1 - (v**2))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title(f'Time for traveling to {x:1.2f} light years away planet\nmeasured from spaceship.')
    ax.set(xlabel='v/c',ylabel='Time [years]')
    ax.set_xlim(0, 1)
    ax.grid(True)
    ax.plot(v, t)
    plt.show()


