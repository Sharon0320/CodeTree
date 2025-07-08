sumlist = []
for i in range(1,5):
    arr = list(map(int,input().split()))
    for j in range(i):
        sumlist.append(arr[j])
print(sum(sumlist))