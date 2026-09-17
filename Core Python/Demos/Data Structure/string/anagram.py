def anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        print("Anagram")
    else:
        print("Not Anagram")

str1 = "listen"
str2 = "silent"

anagram(str1, str2)