def alphabet():
    row = int(input("Enter the number of rows: "))
    for i in range(row):
        k = ord("A") + i  # ASCII KEY
        for j in range(i+1):
            print(chr(k), end=" ")
            k = k+1
        print()


alphabet()
