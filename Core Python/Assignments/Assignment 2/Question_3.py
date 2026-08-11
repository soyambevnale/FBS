print("Convert distance given in feet and inches into meter and centimeter")
feet=int(input("Enter distance in feet : "))
inches=int(input("Enter distance in inches : "))
dist_in_cm=(feet*30.48)+(inches*2.54)
print(f"Distance in cm is : {dist_in_cm}")
dist_in_m=dist_in_cm/100
print(f"Distance in m is : {dist_in_m}")
