class Vehicle:

    def toll(self, person):
        pass


class TwoWheeler(Vehicle):

    def toll(self, person):
        amount = 20

        if person > 2:
            amount = amount + (person - 2) * 10

        return amount


class ThreeWheeler(Vehicle):

    def toll(self, person):
        amount = 30

        if person > 3:
            amount = amount + (person - 3) * 20

        return amount


class FourWheeler(Vehicle):

    def toll(self, person):
        amount = 40

        if person > 4:
            amount = amount + (person - 4) * 40

        return amount


class HeavyVehicle(Vehicle):

    def toll(self, person):
        amount = 60

        if person > 6:
            amount = amount + (person - 6) * 100

        return amount


# Main

print("1. Two Wheeler")
print("2. Three Wheeler")
print("3. Four Wheeler")
print("4. Heavy Vehicle")

choice = int(input("Enter choice : "))
person = int(input("Enter number of persons : "))

if choice == 1:
    v = TwoWheeler()

elif choice == 2:
    v = ThreeWheeler()

elif choice == 3:
    v = FourWheeler()

elif choice == 4:
    v = HeavyVehicle()

else:
    print("Invalid choice")
    exit()

print("Total Toll :", v.toll(person))