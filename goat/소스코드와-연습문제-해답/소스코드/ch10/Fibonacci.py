# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 10장. 분할 정복


#=========================================================
# 피보나치 수열 (분할 정복)
#=========================================================


# 코드 10.8: 분할정복을 이용한 피보나치 수열
def fib(n) :
#    if n==3 : print("fib(3)")

    if n == 0 : return 0		# 정복: 0번째 달
    elif n == 1 : return 1	    # 정복: 1번째 달
    else : 
        return fib(n-1) + fib(n-2)		# 분할과 병합


# 코드 10.9: 행렬 거듭제곱을 이용한 피보나치 수열
from powerMat import *
def fib_mat(n) :
    if n == 0 : return 0        # 정복: 0번째 달
    elif n == 1 : return 1      # 정복: 1번째 달

    mat = [[1,1],[1,0]]         # 초기 피보나치 행렬
    result = powerMat(mat, n)   # 축소정복 방식
    return result[0][1]         # fib(n) 부분을 반환


# 피보나치 수열 테스트 프로그램
n = 31
print('Fibonacci(%d) 거듭제곱     = '%n, fib_mat(n))
print('Fibonacci(%d) 분할정복     = '%n, fib(n))
