"""
The orbit in space of one body around another, such as a planet around the Sun, need
not be circular. In general it takes the formof an ellipse, with the body sometimes closer
in and sometimes further out. If you are given the distance ℓ1 of closest approach that a
planet makes to the Sun, also called its perihelion, and its linear velocity v1 at perihelion,
then any other property of the orbit can be calculated from these two as follows.
   a) Kepler’s second law tells us that the distance ℓ2 and velocity v2 of the planet at
   its most distant point, or aphelion, satisfy ℓ2v2 = ℓ1v1. At the same time the total
   energy, kinetic plus gravitational, of a planet with velocity v and distance r from
   the Sun is given by...
   

"""
# load numpy module
import numpy as np

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
