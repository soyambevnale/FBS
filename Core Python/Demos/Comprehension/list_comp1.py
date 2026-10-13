# li=[ele for ele in range(1,11)]

# print(li)

#list comprehension
li=[1,2,3,4]
result=[ x*2 for x in li]
print(result)

#dictionary comprehension
di={1,2,3,4}
new={x : x*x for x in di}
print(new)

#set comprehension
st={1,2,3,4}
newset={x**3 for x in st}
print(newset)

