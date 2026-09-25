# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

dic={}
start=1
end=int(input("Enter ending : "))
for i in range(1,end+1):
    dic[i]=i*i
    
print(dic)