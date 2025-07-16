n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

for i in range(m):
    sum = 0
    for z in range(queries[i][0],queries[i][1]+1):
        sum += arr[z-1]
    print(sum)