n, m = map(int, input().split())

# Please write your code here.

def factor(n):
    temp = []
    for i in range(1,n+1):
        if (n%i==0):
            temp.append(i)
    return temp

def biggest_factor(a,b):
    set1 = set(a)
    set2 = set(b)
    print(max(set1.intersection(set2)))

biggest_factor(factor(n),factor(m))