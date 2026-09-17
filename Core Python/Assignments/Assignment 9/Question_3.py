# 3. Write a program to reverse a given number using recursive function.
def reverse(n, rev=0):
    if n == 0:
        return rev

    rev = rev * 10 + n % 10
    return reverse(n // 10, rev)


num = int(input("Enter number: "))

res = reverse(num)

print("Reverse =", res)