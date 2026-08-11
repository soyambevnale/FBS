#Write a program to solve the following series :  
# x - x2/3 + x3/5 - x4/7 + …. to n terms 
x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

sum = 0

for i in range(1, n + 1):

    term = (x ** i) / (2 * i - 1)

    if i % 2 == 1:
        sum = sum + term
    else:
        sum = sum - term

print("Sum =", sum)