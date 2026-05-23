# Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following:
# D means deposit while W means withdrawal. i/p - D 300 D 300 W 200 D 100 o/p - 500

option = input("choose option for deposit enter D for Withdrawl enter W and to stop enter Stop  ")
sum = 0 

while option != "Stop":

    if option == "D":
        deposit = int(input("Enter amount- "))
        sum += deposit
    
    elif option == "W":
        withdrwal = int(input("Enter amount- "))
        sum -= withdrwal

    option = input("choose option for deposit enter D for Withdrawl enter W and to stop enter Stop")

print(sum)