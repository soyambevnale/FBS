# 3. Write a program to find the second largest element in the list.
def second(li):
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
            
    print("Second largest :",second)
    
li=[10,20,30,40]
second(li)