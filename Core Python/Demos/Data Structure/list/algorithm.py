# searching element from list

def searchElement(li,sr_element):
    for ind in range(0,len(li)):
        if sr_element==li[ind]:
            return ind
    else:
        return -1
    
    
li=[10,20,30,40,50,60]    
num=int(input("Enter element :"))
res=searchElement(li,num)

#print(res)

if(res!=-1):
    print(f"{num} element present at index {res}")
else:
    print(f"{num} element not present in list")
    
