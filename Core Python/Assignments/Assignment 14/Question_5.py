# 5. Write a Python program to find the longest common prefix of all strings. Use the Python set.

words = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(words[0])):

    s = set()

    for word in words:
        s.add(word[i])

    if len(s) == 1:
        prefix = prefix + words[0][i]
    else:
        break

print(prefix)