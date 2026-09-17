# 6. Write a program to remove duplicates from the list.

def removeDuplicate(li):
    temp=[]
    
    for i in li:
        if i not in temp:
            temp.append(i)
            
    print(temp)
    
li=[10,20,10,50,10]
removeDuplicate(li)