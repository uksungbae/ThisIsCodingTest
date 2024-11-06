"""
시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.
"""

t, m, s = map(str, input().split(':'))

print(m)

"""
틀린 풀이
t, m, s = map(int, input().split(':'))

print(m)

--> 정수형으로 받게 된다면 test case: 01, 02 00등등 0이 제거됨
"""