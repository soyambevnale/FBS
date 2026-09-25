# 2. Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
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


class EnggStudent(Student):

    def __init__(self, studentId, name, age, percentage, branch, internalMarks):
        super().__init__(studentId, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks

    def accept(self):
        super().accept()
        self.branch = input("Enter Branch: ")
        self.internalMarks = float(input("Enter Internal Marks: "))

    def display(self):
        super().display()
        print("Branch :", self.branch)
        print("Internal Marks :", self.internalMarks)

    def calculateRank(self):
        total = self.percentage + self.internalMarks

        if total >= 150:
            return "Distinction"
        elif total >= 120:
            return "First Class"
        elif total >= 100:
            return "Second Class"
        elif total >= 70:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return super().__str__() + \
               ", Branch : " + self.branch + \
               ", Internal Marks : " + str(self.internalMarks)


# Object of EnggStudent
e1 = EnggStudent(101, "Soyam", 21, 80, "Computer", 18)

e1.display()

print("Rank :", e1.calculateRank())

print(e1)