# P=principle amount $
# F=future amount $
# i or r= interest rate
# n=time in years


# the import statement is used to import packages and libraries in our code
#
import numpy as np
from math import e

import math
class Economic_Equivalent:
    def __init__(self):
        print("The Economic Equivalence is Created.")

    def Future(self):
        self.P = int(input("Enter the Principle amount: "))
        self.i = int(input("Enter the interest rate to be used: "))
        self.n = int(input("Enter the time in years: "))
        F=self.P(1+int(self.i))**self.n
        print("The value for the future Amount is ",F)

    def Principle(self):
        self.n = input("Enter the time in years: ")
        self.i = input("Enter the interest rate to be used: ")
        self.F=input("Enter the Future Amount: ")
        P=self.F/(1+self.i)**self.n
        print("The value for Principle is ",P)

    def time_years(self):
        self.P = input("Enter the Principle amount: ")
        self.i = input("Enter the interest rate to be used: ")
        self.F = input("Enter the Future Amount: ")
        ln=np.log
        n=ln(self.F/self.P)/ln(1+self.i)
        print("Time in years is: ",n)


    def interest_rate(self):
        self.P = input("Enter the Principle amount: ")
        self.F = input("Enter the Future Amount: ")
        self.n = input("Enter the time in years: ")
        i=((self.F/self.P)**(1/self.n))-1
        print("The interst rate is: ",i)

Eco=Economic_Equivalent()
Eco.Future()
Eco.Principle()
Eco.time_years()
Eco.interest_rate()











