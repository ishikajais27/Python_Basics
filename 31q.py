def Maxlen(s1, s2):
    if len(s1) < len(s2):
        print(s2)
    elif len(s2) < len(s1):
        print(s1)
    else:
        print(s1 + s2)

s1 = input("Enter 1st string: ")
s2 = input("Enter 2nd string: ")

Maxlen(s1, s2)