# 8. Write a program find reverse of a number 
# without passing parameter without returning value
def rev():
    num=123 
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    print("Reverse : ",rev)
    
rev()

# with passing parameter without returning value
def rev(num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    print("Reverse :",rev)

n=int(input("Enter number :"))
rev(n)

# without passing parameter with returning value
def rev():
    num=123
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    return rev

res=rev()
print("Reverse :",res)

# with passing parameter with returning value
def rev(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev

num=int(input("Enter number :"))
res=rev(num)
print("Reverse :",res)