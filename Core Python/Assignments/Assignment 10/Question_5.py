# 5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

def search(li,ele):
    count=0
    for i in range(0,len(li)):
        if li[i]==ele:
            count+=1
    print("Count : ",count)
    
    for i in range(0,len(li)):
        if li[i]==ele:
            return ele
        
    else:
        return -1
    
    
    
li=[10,20,30,10,25]
ele=10
res=search(li,ele)
if res != -1:
    print("Present  ")
else:
    print("not")
    
        
        
        
        