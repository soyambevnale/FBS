#. 7. Write a program to find sum of digits using recursion. 
def sumSeries(n):
    if n==0:
        return 0
    else:
        return n%10 + sumSeries(n//10)

n=123
res=sumSeries(n)
print(res)
