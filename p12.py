row = int(input('Enter the number'))


for i in range(row + 1):
    print(" " * (row - i) + "*" * (2 * i - 1))