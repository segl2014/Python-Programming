# casting input into integer
marks =  int(input("Enter your Marks:"))

if marks<35:
    print("Grade 'F': Fail")
elif marks >= 35 and marks <= 40:
    print("Grade 'D'")
elif marks >= 41 and marks <= 50:
    print("Grade 'C'")
elif marks >= 50 and marks <= 60:
    print("Grade 'B'")
elif marks >= 60 and marks <=70:
    print("Grade 'B+'")
elif marks >= 70 and marks <=80:
    print("Grade 'A'")
else: # marks > 80-+
    print("Grade 'A+'")
