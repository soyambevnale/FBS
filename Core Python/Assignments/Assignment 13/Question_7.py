# 7. Python Program to Remove the Given Key from a Dictionary

dic={1:10,2:20,3:30}

key=int(input("Enter key : "))

if key in dic:
    print(dic)
    del dic[key]
    print(dic)
else:
    print("Key not exist .")
