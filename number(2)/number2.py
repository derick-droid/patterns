"""
another number shape
"""


def number():
    num = int(input("Enter number: "))
    for i in range(0, num):
        for j in range(0, num):
            print(j + 1, end=" ")


number()
