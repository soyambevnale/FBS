# 1. Write a program to find sum of all elements of list

def sumOfElement(li):
    total=0
    for i in li:
        total+=i
        
    print(total)
    
li=[10,20,30,40]
sumOfElement(li)