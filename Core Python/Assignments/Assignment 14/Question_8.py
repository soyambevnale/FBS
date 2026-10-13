# 8. Write a Python program to find all the anagrams and group them
# together from a given list of strings.

li=["eat", "tea", "tan", "ate", "nat", "bat"]

groups={}
for word in li:
    key="".join(sorted(word))
    if key not in groups:
        groups[key]=[]
        
    groups[key].append(word)
    
print(list(groups.values()))