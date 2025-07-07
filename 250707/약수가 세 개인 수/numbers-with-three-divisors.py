import math

start, end = map(int, input().split())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = 0
for i in range(2, int(math.isqrt(end)) + 1):
    square = i * i
    if square >= start and square < end and is_prime(i):
        count += 1

print(count)