"""
reversed right angle triangle
"""


def triangle():
    row = int(input("Enter row: "))
    for i in range(row, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()

triangle()
