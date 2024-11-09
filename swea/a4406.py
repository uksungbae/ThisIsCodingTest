T = int(input())

for j in range(1, T+1):
    remove_set = {'a','e','i','o','u'}
    word = list(map(str, input()))
    re_w = [i for i in word if i not in remove_set]
    result = str()

    for k in re_w:
        result += k
    print(f"#{j} {result}")
