n = int(input())

for i in range(1, n + 1):
    line = []
    for j in range(1, n + 1):
        line.append(f"{i} * {j} = {i * j}")
    print(", ".join(line))