first_matrix = []
second_matrix = []
sum_matrix = [[[],[],[]],[[],[],[]],[[],[],[]]]

for i in range(3):
    row_data = list(map(int,input().split()))
    first_matrix.append(row_data)

input()

for i in range(3):
    row_data = list(map(int,input().split()))
    second_matrix.append(row_data)

for i in range(3):
    for j in range(3):
        sum_matrix[i][j] = first_matrix[i][j]*second_matrix[i][j]
        print(sum_matrix[i][j],end = " ")
    print()