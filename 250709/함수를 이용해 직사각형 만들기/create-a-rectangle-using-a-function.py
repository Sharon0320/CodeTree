n, m = map(int, input().split())

# Please write your code here.

def make_rectangle(a,b):
    for i in range(a):
        for j in range(b):
            print("1",end="")
        print()

make_rectangle(n,m)