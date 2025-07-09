# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 9장. 억지기법과 탐욕적 전략


#=========================================================
# 코드 9.1: 문자열 매칭(억지기법)

def string_matching( T, P ):		# T는 입력, P는 패턴
    n = len(T)						# n: 입력 문자열의 길이
    m = len(P)						# m: 패턴 문자열의 길이
    for i in range(n-m+1) :			# i: 0, 1, ..., n-m
        j = 0
        while j < m and P[j]==T[i+j] :	# 패턴 문자열을 모두 비교
               j = j + 1
        if j == m :					# 모든 문자가 일치하면, 매칭 성공
            return i				# 현재 위치 반환
    return -1						# 문자열 매칭 실패


# 문자열 매칭(억지 기법) 테스트
text = 'HELLO WORLD'
pattern = 'LO'
print( pattern, 'in', text, '-->', string_matching(text, pattern))
pattern = 'HI'
print( pattern, 'in', text, '-->', string_matching(text, pattern))