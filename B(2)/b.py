"""
block B shape
"""


def b_shape():
    num = int(input("Enter the row: "))
    for row in range(num):
        for col in range(num):
            if (col == 0 and col < 6  and row == 0 or row == 3 or row == 6):
                print("*", end=" ")

        print()

b_shape()



