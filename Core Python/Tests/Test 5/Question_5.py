# 5. Python Program to Find the Union of two Lists without using set concept.

li_1 = [10,20,30,40]
li_2 = [20,30,40,50]

result=[]
for i in li_1:
    if i not in result:
        result.append(i)
        
for i in li_2:
    if i not in result:
        result.append(i)
        
print(result)
    
