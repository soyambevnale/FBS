# 5. Python Program to Count the Number of Vowels in a String

string=" Data "

count=0
for i in string:
    if i in 'aeiou':
        count+=1
        
print(count)