n, m = map(int, input().split())

grid1 = [list(map(int, input().split())) for _ in range(n)]
grid2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    result = []
    for j in range(m):
        if grid1[i][j] != grid2[i][j]:
            result.append(1)
        else:
            result.append(0)
    print(*result)