"""
    Name:       Exercises 2.3
    Purpose:    Transform cartesian coordinates to a polar coordinates
                Using 'math' library
    Authors:    Adrián Hernández & Eider Torres
    Date:       14-08-2021

    Method:
        using transformation equation
        r = (x^2 + y^2)^0.5
        a = atg (y/x)
        be aware about 4 possibilities for 'x', 'y' which gives a
        coordinate in a specific quadrant; it's possible to use
        conditionals for solving this. Note that x cannot be zero, so
        it is necessary consider this case for 'y' positive and negative.
        For reducing lines of code, i'll try to use a general function
        which depends on input values of 'x', 'y'.
"""

# importing atg, sqrt, abs functions and pi constant from math library

from math import atan, sqrt, fabs, pi

# import pyplot from matplotlib library
from matplotlib import pyplot as plt

# ask user to enter x, y values

x = float(input("Enter 'x' coordinate\nx = "))
y = float(input("Enter 'y' coordinate\ny = "))

# defining function

def cartesian2polar(x , y):
    angle = atan(fabs(y/x))
    radius = sqrt((x**2) + (y**2))
    return [radius, angle]

# using conditions for 'x' and 'y' as follows

if x > 0:
    if y > 0:
        #   quadrant 1
        [r,a] = cartesian2polar(x,y)
    elif y < 0:
        #   quadrant 4
        d = 2*pi
        [r,a] = cartesian2polar(x,y)
        a = d - a
    elif y == 0:
        #   positive x axis
        r = x
        a = 0
elif x < 0:
    if y > 0:
        #   quadrant 2
        d = pi
        [r,a] = cartesian2polar(x,y)
        a = d - a
    elif y < 0:
        #   quadrant 3
        d = pi
        [r, a] = cartesian2polar(x, y)
        a = d + a
    elif y == 0:
        #   negative x axis
        r = fabs(x)
        a = pi
elif x == 0:
    if y > 0:
        #   positive y axis
        r = y
        a = pi/2
    elif y < 0:
        #   negative y axis
        r = fabs(y)
        a = (3*pi)/2
    elif 0 == y:
        #   origin
        r = 0
        a = 0

# print computed components

print("\n")
print("     ( x , y )    ->      ( r , a )     ")
print("( %1.3f , %1.3f ) -> ( %1.3f , %1.3f )"%(x,y,r,(a*180/pi)))

# show vector representation using pyplot

# create figure in 'fig' variable

fig = plt.figure()

# create subplot(rows,cols,plot) 'ax1' in 'fig' 

ax1 = fig.add_subplot(1,2,1)
ax1.set_title("Cartesian vector (%1.2f,%1.2f)"%(x,y))
ax1.grid(True)
ax1.set(ylabel="y",xlabel="x")
ax1.axis('square')
ax1.set(xlim=(-1.5*r,1.5*r),ylim=(-1.5*r,1.5*r))

#plot vector in 'ax1'

ax1.quiver(0,0,x,y,angles='xy',scale_units='xy',scale=1,color='red')

# create polar subplot(rows,cols,plot) 'ax2' in 'fig'

ax2 = fig.add_subplot(1,2,2,polar=True)
ax2.set_title("Polar vector (%1.2f,%1.2f)"%(r,a*180/pi))
ax2.grid(True)
ax2.set(ylim=(0,1.5*r))

# plot vector 'ax2'

ax2.quiver(0,0,a,r,angles='xy',scale_units='xy',scale=1,color='red')

# show fig

plt.show()
