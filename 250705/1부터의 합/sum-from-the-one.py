n = int(input())
num = 1
for i in range(2,101):
    if (num + i >= n):
        print(num)
        break
    num += i