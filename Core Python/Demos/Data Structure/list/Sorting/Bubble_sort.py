# def bubbleSort(li):
#     size=len(li)
#     for i in range(1,size):
#         for j in range(0,size-i):
#             if(li[j]>li[j+1]):
#                 li[j],li[j+1]=li[j+1],li[j]
#                 #print(li)
            
# li=[60,50,40,30,20,10]
# print("Before sorting :",li)
# bubbleSort(li)
# print("After sorting :",li)

def bub(li):
    for i in range(len(li)):
        for j in range(len(li)-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    print(li)
li=[3,3,42,454,11,44]
bub(li)
