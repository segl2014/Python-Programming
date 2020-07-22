i = 1
sum = 0
n = int(input("Enter a number:"))
while i<n:
    if(n% i == 0):
        sum =sum + i
        i += 1

        if sum == n:
            print(i,"is a Perfact Number")
        else:
            print(i,"is not a Perfect Number")