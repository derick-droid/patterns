"""
printing number patter
"""


def number():
    row = int(input("Enter row: "))
    for i in range(row):
        for j in range(i + 1):
            print(j + 1, end=" ")

        print()


number()



