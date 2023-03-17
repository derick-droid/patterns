"""
pattern 3
"""


def number():
    num = int(input("Enter row: "))
    for i in range(0, num):
        for j in range(num, 0):
            print(j)


number()
