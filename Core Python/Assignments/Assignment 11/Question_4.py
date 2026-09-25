# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort

def secondLarge(li):
    
    size=len(li) 
    for i in range(size):
        for j in range(size-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    print("Second largest : ",li[-2])

li=[20,10,30,40,70,30,20]
secondLarge(li)