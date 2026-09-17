# 7. Write a program to find sum of digits of a number.
# without passing parameter without returning value
def sod():
    num=123
    total=0
    while num>0:
        digit=num%10
        total=total+digit
        num=num//10
    print("Sum : ",total)   
sod()


# with passing parameter without returning value
def sod(num):
    total=0
    while num>0:
        digit=num%10
        total=total+digit
        num=num//10
    print("Sum : ",total)

n=int(input("Enter number :"))
sod(n)

# without passing parameter with returning value
def sod():
    num=1234
    total=0
    while num>0:
        digit=num%10
        total=total+digit
        num=num//10
    return total

res=sod()
print("Sum : ",res)

# with passing parameter with returning value
def sod(n):
    total=0
    while n>0:
        digit=n%10
        total=total+digit
        n=n//10
    return total

num=int(input("Enter number :"))
res=sod(num)
print("Sum :",res)