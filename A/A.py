"""
A shape
"""


def a_shape():
    num = int(input("Enter the row: "))
    for row in range(0, num + 1):
        for col in range(0, num + 1):
            if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (col > 0 and col<4)):
                print("*", end=" ")
            else:
                print(end=" ")
        print()


a_shape()

