# 11.WAP to check if a given number is Armstrong number or not.For each task create separate functions. 
# without passing parameter without returning value
def arm():
    total=0
    num=153
    temp=num
    count=0
    
    n=num
    while n>0:
        count+=1
        n=n//10
        
    n=num
    while n>0:
        digit=n%10
        total=total+digit ** count
        n=n//10
        
    if temp==total:
        print("Armstrong number .")
    else:
        print("Not armstrong number .")
        
arm()
        
# with passing parameter without returning value
def arm(num):
    temp=num
    total=0
    count=0
    
    n=num
    while n>0:
        count+=1
        n=n//10
        
    n=num
    while n>0:
        digit=n%10
        total=total+digit ** count
        n=n//10
        
    if temp==total:
        print("Armstrong number .")
    else:
        print("Not armstrong number .")
        
n=int(input("Enter number :"))
arm(n)

# without passing parameter with returning value
def arm():
    num=123
    temp=num
    count=0
    total=0
    
    n=num
    while n>0:
        count+=1
        n=n//10
        
    n=num
    while n>0:
        digit=n%10
        total=total+digit ** count
        n=n//10
        
    if temp==total:
        return True
    else:
        return False
    
res=arm()
if res:
    print("Armstrong number .")
else:
    print("Not armstrong number .")
    
# with passing parameter with returning value
def arm(num):
    temp=num
    count=0
    total=0
    
    n=num 
    while n>0:
        count+=1
        n=n//10
        
    n=num
    while n>0:
        digit=n%10
        total=total+digit ** count
        n=n//10
        
    if temp==total:
        return True
    else:
        return False
    
n=int(input("Enter number :"))
res=arm(n)
if res:
    print("Armstrong number .")
else:
    print("Not armstrong number .")
    