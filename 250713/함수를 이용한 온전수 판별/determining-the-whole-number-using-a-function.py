a, b = map(int, input().split())

# Please write your code here.


def is_on(a,b):
    arr = []
    for i in range(a,b+1):
        if (i%2 ==0):
            continue
        if (i%10 == 5):
            continue
        if (i%3 ==0 and i%9 != 0):
            continue
        arr.append(i)
    print(len(arr))

is_on(a,b)