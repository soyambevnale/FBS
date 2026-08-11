print("Calculate Total Salary of Employee")

basic = float(input("Enter basic salary: "))

da = basic * 10 / 100
ta = basic * 12 / 100
hra = basic * 15 / 100

total_salary = basic + da + ta + hra

print(f"Basic Salary : {basic}")
print(f"DA (10%)     : {da}")
print(f"TA (12%)     : {ta}")
print(f"HRA (15%)    : {hra}")
print(f"Total Salary : {total_salary}")