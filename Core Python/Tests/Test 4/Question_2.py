# 2. Write a program to find factorial of given number using recursion

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
        
n=int(input("Enter number : "))
result=fact(n)
print(result)