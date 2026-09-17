# 1. frozenset({})
s1=frozenset({10,20,30,40})
print(type(s1))
print(s1)

# 2. Heterogeneous 
s1=frozenset({10,20,30,40,'abc'})
print(s1)

# 3. Unordered
s1=frozenset({10,20,30,40,50})
print(s1)

# 4.immutable

# 5. unique values are allowed only
s1=frozenset({10,10,20,40,20})
print(s1)