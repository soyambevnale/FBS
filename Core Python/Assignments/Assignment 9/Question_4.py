# 4. Write a program to find sum of n numbers using recursion.
def sumNumbers(n):
    if n == 0:
        return 0

    return n + sumNumbers(n - 1)


n = int(input("Enter n: "))

res = sumNumbers(n)

print("Sum =", res)