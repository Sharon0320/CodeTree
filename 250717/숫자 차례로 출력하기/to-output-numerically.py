n = int(input())

# Please write your code here.

arr = []

for i in range(1,n+1):
    arr.append(i)

rev_arr = []

for j in range(n,0,-1):
    rev_arr.append(arr[j-1])

for x in range(n):
    print(arr[x],end=" ")
print()
for y in range(n):
    print(rev_arr[y],end=" ")