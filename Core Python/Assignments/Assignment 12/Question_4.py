# 4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged

# string="Python"

# li=list(string)
# li[0],li[-1]=li[-1],li[0]

# string=''.join(li)

# print(string)

string="Python"

result=string[-1]+string[1:-1]+string[0]

print(result)