print("Convert days into year , weeks , days")
Days=int(input("Enter days = "))
Year=Days//365
print("Years = ",Year)
Days=Days%365
Weeks=Days//7
print("Weeks = ",Weeks)
Days=Days%7
print("Days = ",Days)
