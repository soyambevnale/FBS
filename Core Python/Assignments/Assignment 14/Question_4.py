# 4. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

li=[10,20,30,40,50,60]

sum=int(input("Enter sum : "))

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==sum:
            print(li[i],li[j])