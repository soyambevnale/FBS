# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

fruits=["apple","banana","mango","apple","apple","banana"]

words=set(fruits)
print("Unique words : ",words)

freq={}
for i in fruits:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
        
print("Frequency of words : ",freq)