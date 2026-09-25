# 2. Write a Python program to remove the intersection of a second set with a first set.

set1={10,20,30,40}
set2={30,40,50,60}

for i in set2:
    if i in set1:
        set1.remove(i)
        
print(set1)