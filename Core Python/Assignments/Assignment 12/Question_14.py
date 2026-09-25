# 14. Python Program to count the occurrences of ach word in a string.

string='data science , data analyst'
word=string.split()
freq={}
for i in word:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
        
print(freq)