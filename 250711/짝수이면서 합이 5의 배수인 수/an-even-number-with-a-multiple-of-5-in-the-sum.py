n = int(input())

# Please write your code here.

def number(n):
    if (n % 2 == 0 and (n%10 + n//10)%5 == 0):
        print("Yes")
    else:
        print("No")

number(n)