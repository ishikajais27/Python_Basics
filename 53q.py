class Rectangle:
    def area(self, length, width):
        return length * width


length = float(input("Enter length: "))
width = float(input("Enter width: "))

r = Rectangle()
print(r.area(length, width))