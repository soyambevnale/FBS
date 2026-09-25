# 1. Write a Python program to find elements in a given set that are not in another set.

set1={10,20,30,40}
set2={30,40,50,60}

for i in set1:
    if i not in set2:
        print(i)
        
    