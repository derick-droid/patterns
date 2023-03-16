"""
another number shape
"""


def number():
    num = int(input("Enter number: "))
    for i in range(0, num):
        for j in range(i, -1, -1):
            print(j + 1, end=" ")
        print()


number()
