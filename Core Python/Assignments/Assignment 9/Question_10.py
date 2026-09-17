# 10. Write a program to reverse a number using recursion. 

def rev(n,reverse):
    if n==0:
        return reverse
    else:
        return rev(n//10,reverse *10+n%10)
    
n=123
reverse=0
res=rev(n,reverse)
print(res)