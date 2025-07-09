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