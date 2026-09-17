# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.
def newList(li):
    temp=[]
    for i in li:
        temp.append(i)
        
    print(temp)
    
li=[2,3,4,5]
newList(li)