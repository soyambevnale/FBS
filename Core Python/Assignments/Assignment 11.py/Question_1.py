# 1. Python Program to Put Even and Odd elements of a List into two Different Lists

def evenOdd(li):
    even=[]
    odd=[]
    for i in li:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
            
    print("Even :",even)
    print("Odd :",odd)
    
li=[10,13,20,23]
evenOdd(li)