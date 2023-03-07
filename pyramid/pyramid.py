"""
pyramid shape
"""


def pyramid():
    row = int(input("Enter the row needed: "))
    for i in range(row):
        for j in range(row):
            print("*", end=" ")
        print()

pyramid()
