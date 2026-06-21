#Define a class named American and its subclass NewYorker.
#Parent class - original class that contains variables and methods.
#class that inherits everything from the parent class.

class American:
    def speak(self):
        print("I am an American")

class NewYorker(American):
    def city(self):
        print("I live in New York")
        
american = American()
newyork = NewYorker()

american.speak()
newyork.speak()
newyork.city()
