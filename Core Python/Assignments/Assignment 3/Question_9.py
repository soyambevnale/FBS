print("Input 5 subject marks from user and display grade .")
sub1=int(input("Enter sub1 marks ="))
sub2=int(input("Enter sub2 marks ="))
sub3=int(input("Enter sub3 marks ="))
sub4=int(input("Enter sub4 marks ="))
sub5=int(input("Enter sub5 marks ="))
total=sub1+sub2+sub3+sub4+sub5
per=total/500*100
print(f"Total :{total}")
print(f"Percentage :{per}")
if(per>=90):
    print("Grade A+")
elif(per>=80):
    print("Grade A")
elif(per>=70):
    print("Grade B")
elif(per>=60):
    print("Grade C")
elif(per>=50):
    print("Grade D")
else:
    print("Grade f")