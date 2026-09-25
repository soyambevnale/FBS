# 6. Python Program to Find the Union of two Lists

def union(li1,li2):
    temp=[]
    for i in li1:
        if i not in temp:
            temp.append(i)
            
    for i in li2:
        if i not in temp:
            temp.append(i)
            
    print("Union of two list : " ,temp)
    
li1=[10,20,30,40]
li2=[30,40,50,60]
union(li1,li2)