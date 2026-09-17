# 6. Write a program to find print the following Fibonacci series using functions: 
# 1  1  2  3 5 8  n terms 

# without passing parameter without returning value
def fib():
    n=7
    a=-1
    b=1
    for i in range(1,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
fib()

# with passing parameter without returning value
def fib(n):
    a=-1
    b=1
    for i in range(1,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
num=int(input("Enter terms :"))
fib(num)

# without passing parameter with returning value
def fib():
    n=7
    a=-1
    b=1
    res=" "
    for i in range(1,n+1):
        c=a+b
        res=res+str(c)+" "
        a=b
        b=c
    return res
        
res=fib()
print(res)

#with passing parameter with returning value
def fib(n):
    a=-1
    b=1
    res=" "
    for i in range(1,n+1):
        c=a+b
        res=res+str(c)+" "
        a=b
        b=c
    return res
        
num=int(input("Enter terms : "))
res=fib(num)
print(res)