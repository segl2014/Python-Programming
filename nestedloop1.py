# multiplicative table from 1 to 10
for x in range(1,11):
    for y in range(1,11):
        print("{0:02d}".format(x*y),end="")
        print();