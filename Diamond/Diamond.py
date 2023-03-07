"""
printing diamond shape
"""


def diamond():
    row = int(input("Enter Row: "))
    for i in range(0, row ):
        for j in range(0, row - i -1):
            print(end=" ")
        for j in range(0, i + 1):
            print("*", end=" ")
        print()

    for i in range(row, 0, -1):
        for j in range(0, row - i):
            print(end=" ")
        for j in range(0, i):
            print("*", end=" ")
        print()


diamond()

