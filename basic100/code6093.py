n = int(input())
arr = list(map(int, input().split()))
result = []

for i in range(n-1, -1, -1):
    result.append(arr[i])

for j in result:
    print(j, end=' ')


"""
for i in range(n-1, -1, -1):
    print(arr[i], end=' ')
"""