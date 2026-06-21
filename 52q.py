import math


class Circle:
    def area(self, radius):
        return math.pi * radius * radius

c = Circle()
r = float(input("Enter radius size - "))
print(c.area(r))