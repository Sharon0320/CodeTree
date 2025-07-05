n = int(input())
num = 0
for i in range(1,101):
    if (num + i >= n):
        print(i)
        break
    num += i