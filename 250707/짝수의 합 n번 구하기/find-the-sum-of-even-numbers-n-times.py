n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    sumn = 0
    odd = []
    for j in range(a,b+1):
        if (j%2 == 0):
            odd.append(j)
    sumn = sum(odd)
    print(sumn)