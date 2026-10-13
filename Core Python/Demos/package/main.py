# 1 . direct import
import mypack.xyz
import mypack.abc
mypack.xyz.greet1()
mypack.abc.greet()
a=mypack.xyz.iname
print(a)

# 2 . from packagename.modulename import member
from mypack.abc import greet
greet()

# 3 from packagename.modulename import members
from mypack.xyz import greet1,iname
greet1()
print(iname)

# 4 from packagename.modulename import all
from mypack.xyz import *
greet1()
print(iname)

# 5 alice  = import packagename.modulename as alicename
import mypack.xyz as a
a.greet1()
print(a.iname)