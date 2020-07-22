x = int(input("Enter value of x:"))
y = int(input("Enter value of Y:"))
print("Before Swapping\n X=",x, "Y=",y)

x= x+y
y=x-y
x=x-y
print("After Swapping\n X=",x,"Y=",y)