n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(n):
    if (arr[i]%2 == 0):
        arr[i] = int(arr[i]/2)

for i in arr:
    print(i,end=" ")