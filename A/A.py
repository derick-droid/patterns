"""
A shape
"""


def a_shape():
    num = int(input("Enter the row: "))
    for row in range(0, num + 1):
        for col in range(0, num + 1):
            if row != 0 or (col == 0 or col == 4) and  (col == 4 and col == 0):
                print("", end=" ")
            else:
                print("*", end=" ")
        print()


a_shape()
