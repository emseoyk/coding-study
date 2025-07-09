# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 6장. 정렬

#=========================================================
# 코드 6.1: 선택 정렬 알고리즘(제자리 정렬 방식)

def selection_sort(A) :
    n = len(A)                              # 리스트의 크기
    for i in range(n-1) :                   # i범위: 0~n-2
        least = i                           # 최소 요소의 인덱스
        for j in range(i+1, n) :            # j의 범위: i+1~n-1
            if (A[j]<A[least]) :            # A[j]가 더 작으면
                least = j                   # least 갱신
        A[i], A[least] = A[least], A[i]	  # A[i]와 A[least] 교환 

        print("  Step %2d ="%(i+1) , A)     # 각 단계별 리스트 변화 출력


# 코드 6.2: 선택 정렬 테스트 프로그램
print("\n선택정렬 테스트")
data = [6,3,7,4,9,1,5,2,8]
print("Original  :", data)
selection_sort(data)
print("Selection :", data)


#=========================================================
# 코드 6.3: 삽입 정렬 알고리즘

def insertion_sort(A) :
    n = len(A)
    for i in range(1, n) :           # i범위: 1~n-1
        key = A[i]                   # A[i]를 key에 저장
        j = i-1                      # 탐색은 i-1부터 앞으로 진행
        while j>=0 and A[j] > key :  # key보다 작은 A[j]가 나올 때 까지 
            A[j + 1] = A[j]          # A[j]를 미리 뒤로 한 칸 옮김
            j -= 1
        A[j + 1] = key               # j+1이 A[i]가 삽입될 위치임

        print("  Step %2d ="%(i+1) , A)     # 각 단계별 리스트 변화 출력



print("\n삽입정렬 테스트")
data = [6,3,7,4,9,1,5,2,8]
print("Original  :", data)
insertion_sort(data)
print("Insertion :", data)

