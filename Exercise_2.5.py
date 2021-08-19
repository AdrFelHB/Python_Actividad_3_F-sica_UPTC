"""
Exercise 2.5 Quantum potential step: Suppose we have a particle with mass equal to the electron mass m = 9.11 ×
10−31 kg and energy 10 eV encountering a potential step of height 9 eV. Write a Python
program to compute and print out the transmission and reflection probabilities using the formulas above.
"""

# load numpy module and pyplot from matplotlib library
import numpy as np
from matplotlib import pyplot as plt
from math import * #import all functions and variables from the package math
#Defining variables
m=float(input("Enter the mass of the particle in MeV/c^2: "))
E=float(input("Enter the initial kinetic energy E of the particle in eV: "))
V=float(input("Enter the potential energy V of the particle in eV: "))
if E<V:
 print("The potential V is greater than the initial energy E and, therefore, the particle never will pass the step")
elif E>V:
 h=6.582119569*(10**-16)
 k1=(sqrt(2*m*(10**-6)*E))/h
 k2=(sqrt(2*m*(10**-6)*(E-V)))/h
 T=(4*k1*k2)/((k1+k2)**2)
 R=((k1-k2)/(k1+k2))**2
 print("The value of T is: ",T)
 print("The value of R is: ",R)

 if T>R:
  print("Therefore, the particle pass the step")
 else:
  print("Therefore, the particle don´t pass the step")
