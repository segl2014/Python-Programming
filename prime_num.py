count = 0                                  #division counter
n = int(input("Enter a number:"))
for  i in range (1, n+1):
    if n % i == 0:
        count += 1
        if count == 2:                     #2 if prime
            print(n, "is a Prime Number")
        else:
            print(n, "is Not a Prime Number")


