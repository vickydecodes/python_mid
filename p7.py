#matrix multiplication


p = int(input("Enter the number of rows for Matrix 1: "))
n = int(input("Enter the number of columns for Matrix 1 (and rows for Matrix 2): "))
q = int(input("Enter the number of columns for Matrix 2: "))

matrix1 = [[int(input()) for _ in range(n)] for _ in range(p)]
matrix2 = [[int(input()) for _ in range(q)] for _ in range(n)]

result = [[0] * q for _ in range(p)]

for i in range(p):
    for j in range(q):
        result[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(n))

for row in result:
    print(*row)


