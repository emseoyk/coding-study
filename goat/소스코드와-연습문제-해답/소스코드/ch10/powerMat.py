# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 10장. 분할 정복


# 코드 10.4: 정방형 행렬 M의 n 거듭제곱 구하기
def powerMat(x, n) :
	if n == 1 :												# 종료조건 
		return x
	elif (n % 2) == 0 :                     				# n이 짝수 
		return powerMat(multMat(x,x), n // 2)
	else :													# n이 홀수
		return multMat(x, powerMat(multMat(x,x), (n - 1) // 2)) 

def multMat(A, B) :
    rows = len(A)
    cols = len(B[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows): 
        for j in range(cols): 
            for k in range(len(B)): 
                result[i][j] += A[i][k] * B[k][j] 

    return result


# 2x2 행렬의 4 거듭제곱 테스트
if __name__ == "__main__":
    fibo = [ [1, 1], [1, 0] ]
    result = powerMat(fibo, 4)
    for r in result: 
        print(r) 
