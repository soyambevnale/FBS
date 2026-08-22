#  Write a program print following patterns: 
# 1 2 3 4 5 
# 2       5
# 3     5
# 4   5
# 5 5

n = 5

for i in range(1, n + 1):

    if i == 1:
        for j in range(1, n + 1):
            print(j, end=" ")
    else:
        print(i, end=" ")

        for j in range(n - i):
            print(" ", end=" ")

        print(n, end="")

    print()