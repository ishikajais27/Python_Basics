#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# i/p - 9      o/p - 11106

a = int(input("Enter number: "))

aa = a * 10 + a

aaa = aa * 10 + a

aaaa = aaa * 10 + a

sum = a + aa + aaa + aaaa

print(sum)