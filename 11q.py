#accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#i/p - 0100,0011,1010,1001 (in decimal - 4, 3, 10,9)     o/p - 1010\
bin = input("Enter 4 digit binary numbers- ").split(",")


#using method to convert binary to decimal
for i in bin:
    
    decimal = int(i, 2)

    if decimal % 5 == 0:

        print(i, end=",")
        



#without usingmethod to convert binary to decimal
for i in bin:

    decimal = 0

    power = 0

    for j in i[::-1]:

        decimal = decimal + int(j) * (2 ** power)

        power += 1

    if decimal % 5 == 0:

        print(i, end=",")