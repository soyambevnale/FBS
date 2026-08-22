# List
# 1 : Denoted by []
li=[10,20,30,40]
print(li)

# 2 : Heterogeneous
li=[10,20,30,3.14,'a']
print(type(li))

# 3 : Ordered 
li=[10,20,30,3.14,'a']
print(li)

# 4 : Mutable
li=[10,20,30,3.14,'a']
li[0]=50
print(li)

# 5 : Duplicate values are allowed
li=[10,20,30,3.14,'a',10,10,10]
print(li)




#### indexing

li=[10,20,30,40,50,60]

print(li[0])                   # subscript
print(li[-1])
print(len(li))                 # total elements
print(li[len(li)-1])



### Traversing 

## Method 1    : Access elements directly 
li=[10,20,30,40,50,60]
for val in li:
    print(val)
    
## Method 2    : Access elements by using index
li=[10,20,30,40,50,60]
for ind in range(0,len(li)):
    print(li[ind])

## python follows zero based indexing because the index represents the distance from
#  the beginning of a sequence