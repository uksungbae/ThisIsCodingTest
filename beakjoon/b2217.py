n = int(input())
rope = []
result = []

for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)

for i in range(n):
    result.append(rope[i] * (i + 1))

print(max(result))