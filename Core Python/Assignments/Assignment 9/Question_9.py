# 9. Write a program to calculate the m to the power n using recursion. 

def power(n,m):
    if m==0:
        return 1
    else:
        return n * power(n,m-1)
    
n=2
m=4
res=power(n,m)
print(res)
    