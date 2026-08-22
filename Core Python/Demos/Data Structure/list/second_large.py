li = [10, 20, 50, 60, 40, 70, 90]

first = li[0]
second = li[0]

for i in range(1, len(li)):
    if li[i] > first:
        second = first
        first = li[i]
    elif li[i] > second and li[i] != first:
        second = li[i]

print("Second Maximum:", second)