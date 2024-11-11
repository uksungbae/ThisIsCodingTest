T = int(input())


for i in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max = 0
    result = 0
    
    for j in range(len(arr)-1,-1,-1):
        if arr[j] > max:
            max = arr[j]
        result += max - arr[j]
    print(f"#{i} {result}")