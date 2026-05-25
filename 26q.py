class Sum:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        
    def sum(self):
        total = self.n1 + self.n2
        print("Sum =", total)


n1 = int(input("Enter 1st num: "))
n2 = int(input("Enter 2nd num: "))

obj = Sum(n1, n2)

obj.sum()