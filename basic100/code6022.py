"""
6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.
"""

arr = list(map(str, input()))

print(arr[0]+arr[1], arr[2]+arr[3], arr[4]+arr[5])


"""
최적의 답
s = input()
print(s[0:2], s[2:4], s[4:6])
"""