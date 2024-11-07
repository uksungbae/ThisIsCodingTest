# 입력
pan = [list(map(int, input().split())) for _ in range(19)]

# 뒤집기 좌표 입력 및 십자 뒤집기 수행
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    
    # 세로줄 뒤집기
    for i in range(19):
        if pan[i][b - 1] == 0:
            pan[i][b - 1] = 1
        else:
            pan[i][b - 1] = 0
    
    # 가로줄 뒤집기
    for i in range(19):
        if pan[a - 1][i] == 0:
            pan[a - 1][i] = 1
        else:
            pan[a - 1][i] = 0

# 출력
for row in pan:
    print(" ".join(map(str, row)))