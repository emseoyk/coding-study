# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 5장 알고리즘 개요

#=========================================================
# 코드 5.4: 세 개의 숫자에서 최댓값을 찾는 알고리즘(파이썬)

def find_max( a, b, c ) :
	max = a		
	if b > max :
	    max = b
	if c > max :
	    max = c
	return max

print("find_max(1, 2, 3) = ", find_max(1, 2, 3))
print("find_max(3, 2, 1) = ", find_max(3, 2, 1))
print("find_max(2, 1, 3) = ", find_max(2, 1, 3))
