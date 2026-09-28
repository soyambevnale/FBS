# 5. Find all of the words in a string that are less than 5 letters (take input from user)

stringg=input("Enter string : ")
li=[ele for ele in stringg.split() if len(ele)<5]

print(li)
