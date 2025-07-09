# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 5장 알고리즘 개요

#=========================================================
# 코드 5.8: 리스트에서 최댓값을 찾는 알고리즘

def find_max( A ):
    n = len(A)              # 입력의 크기
    max = A[0]              # max 초기화
    for i in range(n) :     # 반복 제어부
        if A[i] > max :     # 반복문 내부 -> n번 반복(가장 많이 처리)
            max = A[i]
    return max              # 결과 반환


#=========================================================
# 코드 5.9: 리스트에서 어떤 값을 찾는 알고리즘

def find_key( A, key ):
    n = len(A)              # 입력의 크기
    for i in range(n) :     # 반복 제어부
        if A[i] == key :    # 탐색 성공 --> 인덱스 반환
            return i
    return -1               # 탐색 실패 --> -1 반환



data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("find_max: ", find_max(data))
print("find_key: ", find_key(data, 5))
print("find_key: ", find_key(data, 10))
