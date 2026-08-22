# 5. Sum of all prime numbers between 1 to n

# without passing parameter without returning value

def sop():
    num=10
    total=0
    for i in range(2,num):
        if i%num==0:
            break
        else:
            total+=i
    print(f"Sum of prime number is : {total}")
    
sop()
# # with passing parameter without returning value
# # without passing parameter with returning value
# with passing parameter with returning value