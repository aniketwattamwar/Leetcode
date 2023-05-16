matrix = [[1,1,1],[1,0,1],[1,1,1]]
col = set()
row = set()
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==0:
            col.add(j)
            row.add(i)

for i in row:
    for j in range(len(matrix[0])):
        matrix[i][j]=0
for i in range(len(matrix)):
    for j in col:
        matrix[i][j]=0

print(matrix)