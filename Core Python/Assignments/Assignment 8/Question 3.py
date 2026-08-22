# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# without passing parameter without returning value

def sos():
    num=6
    total=0
    for i in range(1,num+1):
        total=total+i
    print(f"total of series = {total}")
    
sos()

# with passing parameter without returning value

def sos(n):
    total=0
    for i in range(1,n+1):
        total+=i
    print(f"total of series = {total}")

sos(6)
    
# without passing parameter with returning value

def sos():
    num=5
    total=0
    for i in range(1,num+1):
        total=total+i
    return total

res=sos()
print(f"total of series = {res}")



# with passing parameter with returning value
def sos(n):
    total=0
    for i in range(1,n+1):
        total=total+i
    return total

num=int(input("Enter number :"))  
res=sos(num)
print(f"total of series = {res}")

# b. 1!+ 2! + 3! + 4!+..... + n!
# without passing parameter without returning value

def sof():
    fact=1
    total=0
    num=5
    for i in range(1,num+1):
        fact=fact*i
        total+=fact
    print(f"Sum of factorial is = {total}")
    
sof()

# with passing parameter without returning value

def sof(n):
    fact=1
    total=0
    for i in range(1,n+1):
        fact=fact*i
        total+=fact
    print(f"Sum of factorial is = {total}")
    
num=int(input("Enter number : "))
sof(num)

# without passing parameter with returning value

def sof():
    total=0
    fact=1
    num=5
    for i in range(1,num+1):
        fact=fact*i
        total=total+fact
    return total

res=sof()
print(f"Sum of factorial is = {res}")

# with passing parameter with returning value

def sof(n):
    fact=1
    total=0
    for i in range(1,n+1):
        fact=fact*i
        total+=fact
    return total

num=int(input("Enter number : "))
res=sof(num)
print(f"Sum of factorial is = {res}")

## c. 1^1 + 2^2 + 3^3+ ...... n^n

# without passing parameter without returning value

def sum_of_pn():
    total=0
    num=5
    for i in range(1,num+1):
        total=total+i**i
    print(f"Sum of power of number : {total}")

sum_of_pn()

# # with passing parameter without returning value

def sum_of_pn(num):
    total=0
    for i in range(1,num+1):
        total=total+i**i
    print(f"Sum of power of number : {total}")
    
n=int(input("Enter number :"))
sum_of_pn(n)
    
# # without passing parameter with returning value

def sum_of_pn():
    total=0
    num=5
    for i in range(1,num+1):
        total=total+i**i
    return total

res=sum_of_pn()
print(f"Sum of power of number : {res}")

## with passing parameter with returning value

def sum_of_pn(num):
    total=0
    for i in range(1,num+1):
        total=total+i**i
    return total

n=int(input("Enter number :"))
res=sum_of_pn(n)
print(f"Sum of power of number : {res}")