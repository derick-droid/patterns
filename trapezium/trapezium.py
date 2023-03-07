"""
pyramid shape
"""


def pyramid():
    row = int(input("Enter the row needed: "))
    for i in range(0, row):
        for j in range(0, row - i - 1):
            print(end=" ")
        for j in range(0, row + 1):
            print("*", end=" ")
        print()


pyramid()



