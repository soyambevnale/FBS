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

class MedicalStudent(Student):

    def __init__(self, studentId, name, age, percentage, specialization, marksOfInternship):
        super().__init__(studentId, name, age, percentage)
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    def display(self):
        super().display()
        print("Specialization :", self.specialization)
        print("Marks Of Internship :", self.marksOfInternship)

    def accept(self):
        super().accept()
        self.specialization = input("Enter Specialization: ")
        self.marksOfInternship = float(input("Enter Internship Marks: "))

    def calculateRank(self):
        total = self.percentage + self.marksOfInternship

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
               ", Specialization : " + self.specialization + \
               ", Marks Of Internship : " + str(self.marksOfInternship)


# Object
m1 = MedicalStudent(101, "Soyam", 21, 80, "Cardiology", 18)

m1.display()

print("Rank :", m1.calculateRank())

print(m1)