# 3. A list contains sublist with Emp information as follows :
# Data = [[101,”Seema”,45000],[340,”Rajani”,13000],
# [210,”Tannu”,14000],[320,”Suresh”,35000]]
# Write a program to sort the list based on salary.

Data = [[101,"Seema",45000],[340,"Rajani",13000],[210,"Tannu",14000],[320,"Suresh",35000]]
size=len(Data)
for i in range(1,size):
    for j in range(0,size-i):
        if Data[j][2]>Data[j+1][2]:
            Data[j],Data[j+1]=Data[j+1],Data[j]
        
print(Data)