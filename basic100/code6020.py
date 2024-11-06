"""
주민번호는 다음과 같이 구성된다.
XXXXXX-XXXXXXX

왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
주민번호를 입력받아 형태를 바꿔 출력해보자.
"""

a, b = map(str, input().split('-'))

print(a + b)

"""
틀린 풀이
a, b = map(int, input().split('-'))

print(str(a) + str(b))

-> 정수형으로 입력 받는다면 
test case :000907-1121112에서 앞에 0들 생략된다. 따라서 틀림
"""