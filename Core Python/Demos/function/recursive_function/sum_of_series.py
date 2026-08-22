def sOS(n):
    if(n<=0):
        return 0
    else:
        return n+sOS(n-1)
    
num=int(input("Enter Number:"))
res=sOS(num)
print(res)