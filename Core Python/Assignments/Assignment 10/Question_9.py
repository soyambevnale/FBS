# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

def evenOdd(li):
    even=[]
    odd=[]
    for i in li:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
            
    print("Even list :",even)
    print("Odd list :",odd)
    
li=[10,11,20,23,30,45]
evenOdd(li)
