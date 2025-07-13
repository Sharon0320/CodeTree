M, D = map(int, input().split())

# Please write your code here.

month = [31,28,31,30,31,30,31,31,30,31,30,31]

def date(M,D):
    if (M>12):
        return 0
    else:
        if (month[M-1] >= D):
            print("Yes")
        else:
            print("No")

date(M,D)