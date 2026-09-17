# 8. Write a program to check whether a number is prime or not using recursion. 

def checkNumber(n,divisor):
    if divisor==1:
        return "prime"
    elif n%divisor==0:
        return "Not prime"
    else:
        return checkNumber(n,divisor-1)
n=int(input("Enter number :"))
divisor=n-1   
res=checkNumber(n,divisor)
print(res)