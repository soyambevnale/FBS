# print("Firstbit Solutions")
# print('Soyam Bevnale')

# ### Keywords

# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))

# # python 2 = 36
# # python 3 = 35
# # exec = exec()

data=[[101,"Soyam",10000],[102,"Sadi",12000],[202,"sunita",9000]]
size=len(data)
for i in range(1,size):
    for j in range(0, size-i):
        if data[j][2]>=data[j+1][2]:
            data[j][2],data[j+1][2]=data[j+1][2],data[j][2]
print(data)


