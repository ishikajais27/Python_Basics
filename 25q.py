 #   object created from class - instance .  Define a class, which have a class parameter and have a same instance parameter.

class Colour:
    # class parameter
    name = "Unknown"

    def __init__(self, name):
        # instance parameter
        self.name = name


# creating object
s1 = Colour("Black")

print("Class parameter:", Colour.name)
print("Instance parameter:", s1.name)