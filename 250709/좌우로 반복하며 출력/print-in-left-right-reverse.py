n = int(input())
arr = []
for i in range(1,n+1):
    arr.append(i)
for x in range(n):
    for y in range(n):
        print(arr[y],end="")
    print()
    arr.reverse()