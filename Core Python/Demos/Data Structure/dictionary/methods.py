di={1:'Python',2:'Java',3:'C'}

# res=di.clear()
# print(res)

di2=di.copy()
print(di2)

# res=di.get(4,'Key not exist') # if key present then gives output otherwise return second parameter
# print(res)
# # di[4] if key not exist then raise error like key_error

# res=di.items()
# print(res)

# res=di.keys()
# print(res)

# res=di.pop(2)
# print(res)
# print(di)

# res=di.popitem()
# print(res)
# print(di)

res=di.update({3:'Go',5:'R'})
print(di)

res=di.values()
print(res)   