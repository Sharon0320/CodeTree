mul3 = []
mul5 = []
for i in range(10):
    n = int(input())
    if (n % 3 == 0):
        mul3.append(n)
    if (n % 5 == 0):
        mul5.append(n)
print(len(mul3),len(mul5))