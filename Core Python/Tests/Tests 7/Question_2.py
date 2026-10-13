# 2. Write a Python program that takes a list of strings as input and
# returns a new list containing the uppercase versions of the strings
# using list comprehension.

user_string=input("Enter string : ")
new_list=[x for x in user_string.upper().split()]
print(new_list)
