# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance:

    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __del__(self):
        print("Object destroyed")

    def __add__(self, other):
        km = self.km + other.km
        m = self.m + other.m
        cm = self.cm + other.cm

        return Distance(km, m, cm)

    def __sub__(self, other):
        km = self.km - other.km
        m = self.m - other.m
        cm = self.cm - other.cm

        return Distance(km, m, cm)

    def display(self):
        print(self.km, "km", self.m, "m", self.cm, "cm")


d1 = Distance(10, 20, 30)
d2 = Distance(5, 10, 15)

d3 = d1 + d2
print("Addition:")
d3.display()

d4 = d1 - d2
print("Subtraction:")
d4.display()