#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a single line.


# using str method to get the digit of number
for i in range(1000, 3001):

    num = str(i)  

    if (int(num[0]) % 2 == 0 and
        int(num[1]) % 2 == 0 and
        int(num[2]) % 2 == 0 and
        int(num[3]) % 2 == 0):

        print(i, end=",")
        
# without using any method to get the digit of number
for i in range(1000, 3001):

    num = i

    even = True

    while num > 0:

        digit = num % 10

        if digit % 2 != 0:

            even = False
            break

        num = num // 10

    if even:

        print(i, end=",")