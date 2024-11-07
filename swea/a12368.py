tc = int(input())

for i in range(1, tc+1):
    a, b = map(int, input().split())

    if a + b < 24:
        print(f"#{i} {a+b}")
    elif a + b == 24:
        print(f"#{i} 0")
    elif a + b > 24:
        print(f"{i} {b-(24-a)}")