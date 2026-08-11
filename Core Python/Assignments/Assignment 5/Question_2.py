# Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students. 

n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n + 1):

    total = 0

    for j in range(1, 6):
        marks = float(input("Enter marks: "))
        total = total + marks

    percentage = total / 5

    print("Percentage =", percentage)

    total_percentage = total_percentage + percentage

average = total_percentage / n

print("Average Percentage =", average)
    