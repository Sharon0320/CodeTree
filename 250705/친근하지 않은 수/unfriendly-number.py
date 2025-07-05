n = int(input())
arr = []
for i in range(n):
    if (i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
        continue
    arr.append(i)
print(len(arr))