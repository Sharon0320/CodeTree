n = int(input())
num = 1
for i in range(2,101):
    if (num + i >= n):
        print(i)
        break
    num += i