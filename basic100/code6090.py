a, m, d, n = map(int, input().split())

arr = []

arr.append(a)
for i in range(n-1):
    arr.append(arr[i] * m + d)
    

print(arr[n-1])