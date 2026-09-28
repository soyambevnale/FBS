# 4. Remove all of the vowels in a string (take input from user)

string=input("Enter string : ")
li=''.join([ele for ele in string if ele not in 'aeiou'])
print(li)