"""
rectangle shape
"""


def rectangle():
    row =  int(input("Enter row: "))
    for i  in range(row):
        for j in range(row):
            print("*", end=" ")
        print()

rectangle()

