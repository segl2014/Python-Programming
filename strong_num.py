num = int(input("Enter the number:"))
save_num = num
sum = 0
while(num):
    i=1
    p=1
    r= num % 10
    while(i<=r):
        p= p*i
        i += 1
        sum = sum+p
        num = num//10
        if(sum == save_num):
            print(save_num,"is a Strong Number")
        else:
            print(save_num,"is Not a Strong Number")