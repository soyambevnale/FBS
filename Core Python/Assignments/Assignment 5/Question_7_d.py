#Write a program to solve the following series :  
# S = a + a2 / 2 + a3 / 3 + …… + a10 / 10  
a = float(input("Enter value of a: "))

sum = 0

for i in range(1, 11):
    sum = sum + (a ** i) / i

print("S =", sum)