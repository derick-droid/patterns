"""
printing right angle triangle
"""


def right():
    row = int(input("Enter the rows: "))
    for i in range(row):
        for j in range(i + 1):
            print("*", end=" ")
        print()


right()
