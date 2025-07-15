a, b = map(int, input().split())

# Please write your code here.

def program(a,b):
    bigger = max(a,b)
    smaller = min(a,b)

    bigger += 25
    smaller *= 2

    print(smaller,bigger)

program(a,b)