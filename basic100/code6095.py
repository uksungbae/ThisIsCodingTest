#바둑판 설정
pan = [[0] * 19 for _ in range(19)]

#입력
n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    pan[a-1][b-1] = 1

#출력
for i in pan:
    for j in i:
        print(j, end=' ')
    print()