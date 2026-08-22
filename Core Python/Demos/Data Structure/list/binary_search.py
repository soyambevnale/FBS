def binarySearch(li,searchEle):
    beg=0
    end=len(li)-1
    while(beg<=end):
        #print("beg:",beg)
        #print("end:",end)
        mid=(beg+end)//2
        #print("mid:",mid)
        #print("SearchEle:",searchEle)
        #print("mid ele:",li[mid])
        if(searchEle==li[mid]):
            #print("Match condition")
            return mid
        elif(searchEle<li[mid]):
            #print("Less then")
            end=mid-1
        elif(searchEle>li[mid]):
            #print("Greater than")
            beg=mid+1
    else:
        return -1
    
    
ele=int(input("Enter number to find:"))
li=[10,20,30,40,50,60,70]   

res=binarySearch(li,ele)
if(res!=-1):
    print(f"{ele} is present at position {res} .")
else:
    print(f"{ele} not present in list")
        