# How to create custom exception errors -
# Method 1: Create Your Own Exception Class (Most Common) we need to define a class inherited from Exception.
# Method 2: Custom Exception with Constructor - class AgeError(Exception):
#    def __init__(self, message):
#        self.message = message
#try:
#    raise AgeError("Age cannot be negative")
#except AgeError as e:
#    print(e.message)
# Method 3: Inherit from Another Built-in Exception

class CustomError(Exception):
    pass

raise CustomError("Message")