# casting input into integer
age = int(input("Enter your age:"))

# consider 120 upper limit
if age >= 18 and age <= 120:
    print("You are Eligible for Voting")
else:
    print("You are Not Eligible for Voting")