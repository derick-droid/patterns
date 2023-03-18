"""
B shape
"""


def b_shape():
    num = int(input("Enter row: "))
    for row in range(num):
        for col in range(num - 1):
            if (col == 0 or col == 4) or (row == 0 or row == 3 or row == 6) and (col > 0 and col < 4):
                print("*", end=" ")
            else:
                print(end=" ")
        print()


b_shape()


