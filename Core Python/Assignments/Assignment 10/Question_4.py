# 4. Write a program to reverse the list.

def rev(li):
    temp=[]
    for i in range(len(li)-1,-1,-1):
        temp.append(li[i])
        
    print(temp)
    
li=[10,20,30,40]
rev(li)