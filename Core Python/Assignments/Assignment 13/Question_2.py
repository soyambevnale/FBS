# 2. Python Program to Concatenate Two Dictionaries Into One

dic_1={"Name":"Soyam", "Age":21}
dic_2={"a":1 , "Age":25}

for key in dic_2:
    dic_1[key]=dic_2[key]
    
print(dic_1)