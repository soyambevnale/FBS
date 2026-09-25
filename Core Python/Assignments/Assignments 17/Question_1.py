# 1. Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method

class Student:

    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def display(self):
        print("Student ID :", self.studentId)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Percentage :", self.percentage)

    def calculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        elif self.percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return "Student ID : " + str(self.studentId) + \
               ", Name : " + self.name + \
               ", Age : " + str(self.age) + \
               ", Percentage : " + str(self.percentage)


# Parameterized constructor
s1 = Student(101, "Soyam", 21, 85.5)

s1.display()

print("Rank :", s1.calculateRank())

print(s1)
        
        
    
        