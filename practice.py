#!/usr/bin/env python3

################################################
# learning class and basic object oriented 
# this is class company and some method of class
# date : 31.10.19
#################################################

class Company():
    def __init__(self, name, income, employes_amount):
        self.name = name
        self.income = income  
        self.employes_amount = employes_amount

    def show(self):
        print(self.name, self.income, self.employes_amount)

max = Company("max", "2000k", 1400)



Company.show(max)           