matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
for i in range(n):
    for j in range(i + 1, n):
        matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
for i in range(n):
    for j in range(n // 2):
        matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

print(matrix)