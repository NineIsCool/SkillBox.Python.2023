def t(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


n = int(input())
matrix=[]
for i in range(1,n+1):
    matrix.append([i for i in range(1,n+1)])

for line in matrix:
    print(line)
print()
for line in t(matrix):
    print(line)
