import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start, end = map(int, input().split())

count = 0
for i in range(start, end + 1):
    root = int(i ** 0.5)
    if root * root == i and is_prime(root):
        count += 1

print(count)