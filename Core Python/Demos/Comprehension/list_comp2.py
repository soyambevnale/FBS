# even_list=[ele for ele in range(1,11) if ele % 2==0]
# print(even_list)

# Assignment on Comprehension

# 1. Find all of the numbers from 1–1000 that are divisible by 8

# new=[x for x in range(1,1000) if x%8==0]
# print(new)

# # 2. Find all of the numbers from 1–1000 that have a 6 in them

# new=[x for x in range(1,1000) if '6' in str(x)]
# print(new)

# # 3. Count the number of spaces in a string (take input from user)

# string=input("Enter string : ")
# new=[x for x in string if x==" " ]
# print(len(new))

# # 4. Remove all of the vowels in a string (take input from user)

# string=input("Enter string : ")
# new=[x for x in string if x not in 'aeiouAEIOU']
# print(new)

# # 5. Find all of the words in a string that are less than 5 letters (take
# # input from user)

# string=input("Enter string : ")
# res=string.split()
# new=[x for x in res if len(x)<5]
# print(new)

# 6. Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)

# string=input("Enter string : ")
# res=string.split()
# new={x:len(x) for x in res}
# print(new)

# 7. Use a nested list comprehension to find all of the numbers from
# 1–1000 that are divisible by any single digit.
new=[[z for z in range(1,1001) if any(z%x==0 for x in range(2,10))]]
print(new)