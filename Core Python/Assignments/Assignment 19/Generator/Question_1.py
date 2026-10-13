# 1 We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def fib(n):
    a=-1
    b=1
    for i in range(1,n+1):
        c=a+b
        yield c
        a=b
        b=c
        
n=5
res=fib(n)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
    

        