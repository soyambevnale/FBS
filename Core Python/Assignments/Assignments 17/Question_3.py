# 3. Create a class MedicalStudent inherited from Student with following
# :

# i. Data members :Specialization
# ii. MarksOfInternship
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
        else:
            return "Pass"

    def __str__(self):
        return self.name


class MedicalStudent(Student):

    def __init__(self, studentId, name, age, percentage,
                 specialization, marksOfInternship):

        super().__init__(studentId, name, age, percentage)

        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    def display(self):
        super().display()
        print("Specialization :", self.specialization)
        print("Marks Of Internship :", self.marksOfInternship)

    def calculateRank(self):
        total = self.percentage + self.marksOfInternship

        if total >= 150:
            return "Distinction"
        elif total >= 120:
            return "First Class"
        elif total >= 100:
            return "Second Class"
        else:
            return "Pass"

    def __str__(self):
        return super().__str__() + \
               ", Specialization : " + self.specialization + \
               ", Internship Marks : " + str(self.marksOfInternship)


m1 = MedicalStudent(101, "Soyam", 21, 80, "Cardiology", 18)

m1.display()

print("Rank :", m1.calculateRank())

print(m1)