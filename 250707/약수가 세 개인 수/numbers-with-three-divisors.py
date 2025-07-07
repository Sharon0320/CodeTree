start, end = map(int, input().split())

# Please write your code here.
result = []
for i in range(start,end):
    temp = []
    for j in range(1,i+1):
        if (i%j == 0):
            temp.append(j)
    if (len(temp) == 3):
        result.append(i)
print(len(result))