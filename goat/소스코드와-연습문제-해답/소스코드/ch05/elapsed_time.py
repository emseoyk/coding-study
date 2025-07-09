# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 5장 알고리즘 개요

#=========================================================
# 코드 5.5: time 모듈을 이용한 실행시간 측정 예

def find_max( a, b, c ) :
	max = a		
	if b > max :
	    max = b
	if c > max :
	    max = c
	return max



import time			# time 모듈 불러오기

start = time.time()		# 현재 시각을 start에 저장(시작 시각)
#testAlgorithm(input)		# 실행시간을 측정하려는 알고리즘 호출
for _ in range (1000000): 
	find_max(2, 1, 3)
end = time.time()			# 현재 시각을 end에 저장(종료 시각)
print("실행시간 = ", end-start)	# 실제 실행시간(종료-시작)을 출력