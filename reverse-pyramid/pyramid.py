""""
reverse pyramid
"""


def reverse():
    row = int(input("Enter row: "))
    for i in range(row, 0, -1):
        for j in range(0, row - i):
            print(end=" ")
        for j in range(0, i):
            print("*", end=" ")
        print()


reverse()
