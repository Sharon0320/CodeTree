a, b = map(int, input().split())

# Please write your code here.

def program(a,b):
    arr = []
    for i in range(a,b+1):
        prime = []
        for j in range(1,i+1):
            if (i%j == 0):
                prime.append(j)
        if (len(prime) == 2):
            if (((i//10) + (i%10))%2 == 0):
                arr.append(i)
    print(len(arr))

program(a,b)