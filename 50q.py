# @staticmethod → method belongs to class, not object, Can be called using class name directly, No need to use self,It does NOT depend on object
# data. It is just a utility function inside a class
class American:
    
    @staticmethod
    def static_method():
        print("American")

# calling static method
American.static_method()