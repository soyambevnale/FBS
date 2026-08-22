# 4. Sum of all odd numbers between 1 to n

# without passing parameter without returning value

def sum_of_odd():
    num=10
    total=0
    for i in range(1,num+1):
        if i%2!=0:
            total+=i
    print(f"Sum of odd numbers : {total}")
    
sum_of_odd()
            
# # with passing parameter without returning value

def sum_of_odd(n):
    total=0
    for i in range(1,n+1):
        if i%2!=0:
            total+=i
    print(f"Sum of odd numbers : {total}")
    
num=int(input("Enter number : " ))
sum_of_odd(num)

# # without passing parameter with returning value

def sum_of_odd():
    num=10
    total=0
    for i in range(1,num+1):
        if i%2!=0:
            total+=i
    return total

res=sum_of_odd()
print(f"Sum of odd numbers : {res}")

# with passing parameter with returning value

def sum_of_odd(n):
    total=0
    for i in range(1,n+1):
        if i%2!=0:
            total+=i
    return total

num=int(input("Enter number  : "))
res=sum_of_odd(num)
print(f"Sum of odd numbers : {res}")