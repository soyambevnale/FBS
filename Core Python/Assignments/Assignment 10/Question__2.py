# 2. Write a program to find maximum and minimum element in a list.

def largest(li):
    first=li[0]
    second=li[1]
    if first<second:
        second=first
        first=li[1]
        
    for i in range(1,len(li)):
        if li[i]>first:
            second=first
            first=li[i]
        elif li[i]>second and li[i]!=first:
            second=li[i]
            
    print("largest :",first)
    
li=[10,20,30,40]
largest(li)


def smallest(li):
    first=li[0]
    second=li[1]
    if first>second:
        second=first
        first=li[1]
        
    for i in range(1,len(li)):
        if li[i]<first:
            second=first
            first=li[i]
        elif li[i]<second and li[i]!=first:
            second=li[i]
            
    print("smallest :",first)
    
li=[10,20,30,40]
smallest(li)
