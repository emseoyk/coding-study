# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 1장 스택

#=========================================================
# 코드 1.7: 반복 구조의 팩토리얼 함수

def factorial_iter(n) :
    result = 1
    for k in range(2, n+1) :	# k: 2, ..., n
        result = result * k	# result에 반복적으로 곱함
    return result


#=========================================================
# 코드 1.8: 순환 구조의 팩토리얼 함수

def factorial(n) :		# 순환적으로 구현한 factorial 함수
    if n == 1 : return 1		# 종료 조건: 순환을 멈추는 부분
    else :
        return n * factorial(n - 1)	# 자신을 순환적으로 호출



print('Factorial순환(3) = ', factorial(3))
print('Factorial반복(3) = ', factorial_iter(3))

print('Factorial순환(10) = ', factorial(10))
print('Factorial반복(10) = ', factorial_iter(10))



a = 10
print(type(a))      # int
a = 10.0
print(type(a))      # float
print(type(123))    # int
print(type(123.0))  # float
print(type("123"))  # str
print(type(True))   # bool
print(type(1+2j))   # complex
