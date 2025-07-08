matrix = []

for i in range(3):
    row_data = list(map(int,input().split()))
    matrix.append(row_data)
    for j in range(3):
        matrix[i][j] = matrix[i][j]*3
        print(matrix[i][j],end = " ")
    print()