#!/usr/bin/env python3

class Company():
    def __init__(self, name, income, employes_amount):
        self.name = name
        self.income = income  
        self.employes_amount = employes_amount

    def show(self):
        print(self.name, self.income, self.employes_amount)

max = Company("max", "2000k", 1400)



Company.show(max)           