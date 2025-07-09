# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 6장. 정렬


#=========================================================
# 코드 6.4: 퀵 정렬 알고리즘

def quick_sort(A, left, right) :
    if left<right :		    			# 정렬 범위가 2개 이상인 경우
        q = partition(A, left, right)	# 좌우로 분할 
        quick_sort(A, left, q - 1)		# 왼쪽 부분리스트를 퀵 정렬
        quick_sort(A, q + 1, right)		# 오른쪽 부분리스트를 퀵 정렬


# 코드 6.5: 분할 알고리즘
def partition(A, left, right) :
	low = left + 1			
	high = right			
	pivot = A[left] 		
	while (low < high) :	
		while low <= right and A[low] <= pivot :
			low += 1
		while high >= left and A[high] > pivot :
			high-= 1

		if low < high :
			A[low], A[high] = A[high], A[low]

	A[left], A[high] = A[high], A[left]
	return high


data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7]		# 입력 리스트
print("Original  : ", data)				# 만들고 모든 항목을 0으로 초기화
quick_sort(data, 0, len(data)-1)        # 퀵 정렬
print("QuickSort : ", data)
