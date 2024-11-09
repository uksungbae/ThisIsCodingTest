TC = int(input())

for i in range(1, TC+1):
    a, b = map(int, input().split())

    if a > 9 or b > 9:
        print(f"#{i} -1")
    else:
        print(f"#{i} {a*b}")