a, b = map(int, input().split())

# Please write your code here.
def is_prime(n):
    lo = []
    for i in range(1,n+1):
        if (n%i == 0):
            lo.append(i)
    if(len(lo) == 2):
        return True
    else:
        return False


arr = []
for i in range(a,b+1):
    if (is_prime(i)):
        arr.append(i)

print(sum(arr))