# 12. Python Program to count number of lowercase characters in a string.

string='Data Science'
count=0
for i in string:
    if i.islower():
        count+=1

print(count)
        