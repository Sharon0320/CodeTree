five = []
for i in range(4):
    a,b,c,d = map(int,input().split())
    if (a % 5 == 0):
        five.append(a)
    if (b % 5 == 0):
        five.append(a)
    if (c % 5 == 0):
        five.append(a)
    if (d % 5 == 0):
        five.append(a)
print(len(five))