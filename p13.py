#Inverted full pyramid

rows = int(input('Enter the rows'))


for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)
