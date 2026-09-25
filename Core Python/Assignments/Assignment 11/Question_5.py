# 5. Python Program to Sort a List According to the Length of the Elements within the list.

def sortList(li):
    for i in range(len(li)):
        for j in range(len(li)-1):
            if len(li[j])>len(li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
                
    print("Sorted using len : ",li)
    
li = ["apple", "cat", "banana", "hi", "orange"]
sortList(li)