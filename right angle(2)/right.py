def right():
    k = 1
    row = int(input("Enter number of row: "))
    for i in range(1, row):
        for j in range(1, k+1):
            print("*", end=" ")
            k = k + 1
        print()


right()





