# 7. Python Program to Find the Intersection of Two Lists

def intersection(li1,li2):
    temp=[]
    for i in li1:
        if i in li2 and i not in temp:
            temp.append(i)
                
    print("Intersection of two list : " , temp)
    
li1=[10,20,30,40]
li2=[20,30,50,60]
intersection(li1,li2)