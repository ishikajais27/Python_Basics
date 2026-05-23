#Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class StringMethods:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    
    def getString(self):
        self.s=input("Enter the string")
        
    def printString(self):
        print(self.s.upper())
        print(self.name.upper())
        print(self.gender.upper())
 
 
obj = StringMethods("Ishika","F")
obj.getString()
obj.printString()