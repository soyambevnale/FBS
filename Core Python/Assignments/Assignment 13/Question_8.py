# 8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

string="Data Science , Data Analyst"

freq={}
word=string.split()

for i in word:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
        
print(freq)