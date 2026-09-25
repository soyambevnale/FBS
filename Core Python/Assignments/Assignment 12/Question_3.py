# 3. Python Program to Detect if Two Strings are Anagrams

string_1="listen"
string_2="silent"

if len(string_1)==len(string_2):
    
    for i in string_1:
        if string_1.count(i)!=string_2.count(i):
            print("Not Anagram")
            break
    else:
        print("Anagram")
            
else:
    print("Not Anagram")
    