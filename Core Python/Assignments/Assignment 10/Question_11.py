# 11. Write a program to print all numbers which are divisible by m and n in the list.
def division(li,m,n):
    temp=[]
    for i in li:
        if i%m==0 and i%n==0:
            temp.append(i)
            
    print(temp)
    
li=[10,12,13,16,18]
m=2
n=3
division(li,m,n)