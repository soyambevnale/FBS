print("Print fibonacci series.")
n = int(input("Enter number of terms: "))

a = -1
b = 1

for i in range(1,n+1):
    c = a + b
    print(c, end=" ")
    a = b
    b = c