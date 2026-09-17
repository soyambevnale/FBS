li=[[10,20],[30,50]]

li.append(30)
print(li)

li.extend([30,50])
print(li)

li.insert(1,90)
print(li)

import copy
b=li.copy()
b[0][0]=2

print(b)
print(li)