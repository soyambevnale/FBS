# 1
import demo1
demo1.add(12,4)
print(demo1.pname)

# 2
from demo1 import add
add(12,3)

# 3
from demo1 import add,pname
add(13,4)
print(pname)

#4
from demo1 import *
add(17,2)
print(pname)

# 5 Alice name
import demo1 as d
d.add(1,2)
print(d.pname)