n = int(input())
arr = list(map(int, input().split()))
result = []

for i in range(1, 24):
    result.append(arr.count(i))
    #result.insert(i, arr.count(i))
    

for j in result:
    print(j, end=' ')

# print(" ".join(map(str, result)))
