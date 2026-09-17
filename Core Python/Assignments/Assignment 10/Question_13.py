# 13 . Write a program to print list after removing even numbers.

def removeEven(li):
    temp=[]
    for i in li:
        if i%2!=0:
            temp.append(i)
            
    print("After remove even numbers :",temp)
    
li=[10,12,13,15]
removeEven(li)
            