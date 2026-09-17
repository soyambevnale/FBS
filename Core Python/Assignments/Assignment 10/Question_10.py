# 10. Write a program to remove all occurrences of a given element in the list.

def removeElement(li,ele):
    temp=[]
    for i in li:
        if i!=ele:
            temp.append(i)
    print(temp)
    
li=[10,20,10,20,30,50]
ele=10
removeElement(li,ele)
            