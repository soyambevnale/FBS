# 7. Write a program to create a new list from existing list which contains cube of
# each number of list.

def cube(li):
    temp=[]
    for i in li:
        temp.append(i**3)
        
    print(temp)
    
li=[2,3,4,5]
cube(li)