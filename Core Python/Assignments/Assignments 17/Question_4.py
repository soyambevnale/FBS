# 4. Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method

class College:

    def __init__(self, noOfStudents):
        self.students = []

    def addStudent(self, student):
        self.students.append(student)

    def getStudent(self, studentId):
        for student in self.students:
            if student.studentId == studentId:
                return student

        return None

    def removeStudent(self, studentId):
        for student in self.students:
            if student.studentId == studentId:
                self.students.remove(student)
                print("Student removed successfully")
                return

        print("Student not found")

    def __str__(self):
        result = ""

        for student in self.students:
            result = result + str(student) + "\n"

        return result


# Creating students
s1 = Student(101, "Soyam", 21, 85)
s2 = Student(102, "Riya", 22, 75)
s3 = Student(103, "Amit", 21, 65)


# Creating College
c = College(3)

# Adding students
c.addStudent(s1)
c.addStudent(s2)
c.addStudent(s3)

# Display all students
print(c)

# Get student
student = c.getStudent(102)

if student != None:
    print("Student Found:")
    print(student)

# Remove student
c.removeStudent(101)

# Display after removing
print("After removing:")
print(c)