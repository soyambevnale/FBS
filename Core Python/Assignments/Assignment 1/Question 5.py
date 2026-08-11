print("To calculate Compound Interest ")
Principal=int(input("Enter Principal = "))
Rate=int(input("Enter Rate = "))
Time=int(input("Enter Time = "))
Amount=Principal*((1+Rate / 100) ** Time)
CI=Amount-Principal
print("Compound Interest is = ",CI)
print("Compound Interest is = ",round(CI,2))