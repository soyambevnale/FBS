print("To check if given number Strong Number.")
n = int(input("Enter a number: "))

temp = n
sum = 0

while temp > 0:            #145
    digit = temp % 10      #145%10=5
    fact = 1               #

    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact       
    temp = temp // 10      #145//10=14

if sum == n:
    print("Strong Number")
else:
    print("Not Strong Number")