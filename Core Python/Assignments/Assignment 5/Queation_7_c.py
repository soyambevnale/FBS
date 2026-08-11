#Write a program to solve the following series :  
# Find the sum of a geometric series from 1 to n where the common ratio is 2. 
n = int(input("Enter number of terms: "))

term = 1
sum = 0

for i in range(n):
    sum = sum + term
    term = term * 2

print("Sum =", sum)