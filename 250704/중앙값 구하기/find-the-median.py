a,b,c = map(int,input().split())
lis = [a,b,c]
lis.remove(max(lis))
lis.remove(min(lis))
print(lis[0])