# 3. Python Program to Sort the List According to the Second Element in Sublist

def secondEle(li):
    size=len(li)
    for i in range(size):
        for j in range(size-1):
            if li[j][1]>li[j+1][1]:
                li[j],li[j+1]=li[j+1],li[j]
                
    print(li)
    
li=[[10,40],[20,30]]
secondEle(li)