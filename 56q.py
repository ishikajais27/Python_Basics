# except - means If an error happens, don't crash. Come here. try - Python, please try to run this code run when no error occurs 

def divide():
    return 5 / 0

try:
    divide()

except ZeroDivisionError:
    print("Cannot divide by zero")