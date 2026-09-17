#1
tu=(10,20)
print(type(tu))

#2  Heterogeneous
tu=(10,3.14,'abc')
print(tu)

#3 ordered
tu=(10,'abc',3.14)
print(tu)

#4 immutable
tu=(10,20,30)
# tu[0]=40
print(tu)

#5 duplication allowed
tu=(10,20,10)
print(tu)

#6 faster than list
import sys
tu=(10,20)
print(sys.getsizeof(tu))