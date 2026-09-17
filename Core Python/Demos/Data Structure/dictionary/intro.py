# 1 = { }

di={1:10,2:'abc','zyx':3.14}
print(type(di))
print(di)

# 2 = heterogeneous
di={1:10,2:'abc','zyx':3.14}
print(type(di))
print(di)

# 3 = Sequence = Ordered since 3.7
di={1:10,2:'abc','zyx':3.14,2:'c','zyx':6.7}
print(type(di))
print(di)

# 4 = changeable
## key = mutable  , val = immutable
di[3]=234
print(di)

# 5 = duplication
## keys = uniques , val = duplicated
print(di)
