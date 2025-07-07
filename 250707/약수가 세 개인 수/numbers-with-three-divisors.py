start, end = map(int, input().split())

result = []
for i in range(start, end):  # end는 포함 안 되므로 그대로 둠
    temp = []
    for j in range(1, i + 1):  # 1부터 i까지 모든 수로 나누어 보기
        if i % j == 0:
            temp.append(j)  # 약수를 temp에 저장
    if len(temp) == 3:  # 약수가 정확히 3개면 조건 만족
        result.append(i)

print(len(result))  # 조건 만족하는 수의 개수 출력
