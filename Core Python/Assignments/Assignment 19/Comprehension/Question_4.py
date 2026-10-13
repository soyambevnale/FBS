# 4. Remove all of the vowels in a string (take input from user)

string=input("Enter string : ")
li=[ele for ele in string if ele not in 'aeiouAEIOU']
print(li)