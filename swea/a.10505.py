T = int(input())

for i in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    avg = float(sum(arr)/n)
    under_avg = 0

    for j in arr:
        if j <= avg:
            under_avg += 1

    print(f"#{i} {under_avg}")