# 2. Python Program to Merge Two Lists and Sort it

def mergeSort(li1,li2):
    temp=[]
    for i in li1:
        temp.append(i)
        
    for i in li2:
        temp.append(i)
        
    print("Merge List : ",temp)
    
    size=len(temp)
    
    for i in range(size):
        for j in range(size-1):
            if temp[j]>temp[j+1]:
                temp[j],temp[j+1]=temp[j+1],temp[j]
                
    print(temp)
    
li1=[11,14,45]
li2=[40,50,20]

mergeSort(li1,li2)
            
            
        
    
    