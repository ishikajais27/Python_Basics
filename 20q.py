class Num:

    def generate(self, n):

        if n == 0:
            return

        if n % 7 == 0:
            print(n)

        self.generate(n - 1)


obj = Num()

N = int(input("Enter num - "))

obj.generate(N)