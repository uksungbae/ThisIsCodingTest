tc = int(input())

for i in range(1, tc+1):
    l, u, x = map(int, input().split())

    if l > x:
        print(f"#{i} {l-x}")
    elif x >= l and u >= x:
        print(f"#{i} 0")
    elif x > u:
        print(f"#{i} -1")