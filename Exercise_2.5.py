"""
Exercise 2.5 Quantum potential step: Suppose we have a particle with mass equal to the electron mass m = 9.11 ×
10−31 kg and energy 10 eV encountering a potential step of height 9 eV. Write a Python
program to compute and print out the transmission and reflection probabilities using the formulas above.
"""

#Load numpy module and pyplot from matplotlib library
import numpy as np
from matplotlib import pyplot as plt
#import all functions and variables from the package math
from math import * 
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
 print("The probability that the particle is reflected is: ",round((R*100),2),"%") #Print the percent probability that particle will be reflected
