# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 10장. 분할 정복

#=========================================================
# k번째 작은 수 찾기 문제
#=========================================================

# 정렬을 이용한 방법
def kth_smallest_sort(A, k): 
    A.sort() 
    return A[k-1] 

  
# 코드 10.5: 분할정복을 이용한 k번째 작은 수 찾기
def quick_select(A, left, right, k): 
    pos = partition(A, left, right) 	# A에서 피벗의 인덱스
    print(A)

    if (pos+1 == left+k):				# case 1: 찾음. 완료.
        return A[pos] 
    elif (pos+1 > left+k):				# case 2: 답은 왼쪽 부분리스트에. 
        return quick_select(A, left, pos-1, k) 
    else : 							# case 3: 답은 오른쪽 부분리스트에.
        return quick_select(A, pos+1, right, k-(pos+1-left)) 


def partition(A, left, right) :
	low = left + 1				    # 왼쪽 부분 리스트의 인덱스 (증가방향)
	high = right					# 오른쪽 부분 리스트의 인덱스 (감소방향)
	pivot = A[left] 				# 피벗 설정 
	while (low <= high) :			# low와 high가 역전되지 않는 한 반복 
	    while low <= right and A[low] <= pivot : low += 1
	    while high>= left  and A[high] > pivot : high-= 1

	    if low < high :			    # 선택된 두 레코드 교환 
	        A[low], A[high] = A[high], A[low]

	A[left], A[high] = A[high], A[left]	# 마지막으로 high와 피벗 항목 교환 
	return high					    # 피벗의 위치 반환

# 테스트 프로그램
org = [27, 4, 26, 23, 34, 13, 42, 22, 48]
n = len(org) 
array = list(org)
print("입력 리스트 =", array) 
print("[축소정복] 최솟값: ", quick_select(array, 0, n-1, 1))
print()

array = list(org)
print("[축소정복] 최댓값: ", quick_select(array, 0, n-1, n)) 
print()

array = list(org)
print("[축소정복] 중앙값: ", quick_select(array, 0, n-1, 1+(n-1)//2)) 
print()

array.sort()
print("정렬 리스트 =", array) 

array = [6, 5, 7, 9, 18, 3, 8]
n = 7
print("[축소정복] 중앙값: ", quick_select(array, 0, n-1, 1+(n-1)//2)) 
print()



