def selection(li):
    size=len(li)
    for i in range(0,size-1):
        min_ind=i
        for j in range(i+1,size):
            if (li[j]<li[min_ind]):
                min_ind=j
            li[j],li[min_ind]=li[min_ind],li[j]
    print(li)
    
li=[10,40,20,30]
selection(li)