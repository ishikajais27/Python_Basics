# Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]

#C is 50. H is 30.D is the variable whose values should be .
#ip = 100,150,180   o/p- 18,22,24   

import math
class SqRoot:
    def __init__(self):
        self.C = 50
        self.H = 30
        self.D = map(int, input("Enter valuesof D- ").split(","))  #new concept of map to take input(integer type) from user in a comma-separated sequence
    def calc(self):
       for i in self.D:
            Q = math.sqrt((2 * self.C * i) / self.H)

            print(int(Q)) 
obj = SqRoot()
obj.calc()