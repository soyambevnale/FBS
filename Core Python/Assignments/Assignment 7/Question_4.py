#  Write a program print following patterns:
#         1 
#       2 3 2 
#     3 4 5 4 3 
#   4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5 


n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print(i + j - 1, end=" ")

    for j in range(i - 1, 0, -1):
        print(i + j - 1, end=" ")

    print()