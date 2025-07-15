a, b = map(int, input().split())

# Please write your code here.

def program(a,b):
    if (a<b):
        a+=10
        b*=2
    else:
        b+=10
        a*=2

    print(a,b)

program(a,b)