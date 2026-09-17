# 2. Write a program to check if given number is Armstrong or not using recursive function. 
def countDigits(n):
    if n == 0:
        return 0
    return 1 + countDigits(n // 10)


def armstrong(n, digits):
    if n == 0:
        return 0

    return (n % 10) ** digits + armstrong(n // 10, digits)


num = int(input("Enter number: "))

digits = countDigits(num)
res = armstrong(num, digits)

if res == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")