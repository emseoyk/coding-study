# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 11장. 동적 계획법

#=========================================================
# 피보나치 수열 (동적 계획법)
#=========================================================

# 코드 11.1: 피보나치 수열(메모이제이션 이용)
def fib_dp_mem(n) :
    if mem[n] == None :		    # 풀리지 않은 경우-> 계산하고 저장
        if n < 2 :
            mem[n] = n			# 기반 상황: n<=1
        else: 					# 일반 상황: otherwise
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)	
    return mem[n]


# 코드 11.2: 피보나치 수열(테이블화 이용)
def fib_dp_tab(n) :
    f = [None] * (n+1)			# 테이블을 만들고
    f[0] = 0					# 기반 상황 처리
    f[1] = 1					# 기반 상황 처리
    for i in range(2, n + 1):	# 상향식으로: 2, 3, ... n
        f[i] = f[i-1] + f[i-2]	# 부분 문제들을 해결하고 저장함
    return f[n]					# 결과 반환


# 피보나치 수열(분할 정복)
def fib(n) :
    if n == 0 : return 0		# 정복: 0번째 달
    elif n == 1 : return 1	    # 정복: 1번째 달
    else : 
        return fib(n-1) + fib(n-2)		# 분할과 병합

# 피보나치 수열(반복 구조)
def fib_iter(n) :
	if (n < 2): return n
	last = 0
	current = 1
	for i in range(2, n+1) :
		tmp = current
		current += last
		last = tmp
	return current


# 피보나치 수열 테스트 프로그램
n = 8
print('Fibonacci(%d) 분할정복     = '%n, fib(n))
print('Fibonacci(%d) 테이블화     = '%n, fib_dp_tab(n))
mem = [None] * (n+1)			# 테이블을 만들고
print('Fibonacci(%d) 메모이제이션 = '%n, fib_dp_mem(n))
print('Fibonacci(%d) 반복 구조    = '%n, fib_iter(n))
