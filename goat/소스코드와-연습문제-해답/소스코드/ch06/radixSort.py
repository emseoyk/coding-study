# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 6장. 정렬


#=========================================================
# 코드 6.6: 기수 정렬 알고리즘

from collections import deque

def radix_sort(A) :
    queues = []                             
    for i in range(BUCKETS) :               
        queues.append(deque())              

    n = len(A)
    factor = 1                              
    for d in range(DIGITS) :                
        for i in range(n) : 	            
            queues[(A[i]//factor) % BUCKETS].append(A[i])

        i = 0
        for b in range(BUCKETS) :		    
            while queues[b] :               
                A[i] = queues[b].popleft()  
                i += 1
        factor *= BUCKETS					
        print("step", d+1, A)



#=========================================================
# 코드 6.7: 기수 정렬 테스트 프로그램

import random       
BUCKETS = 10        
DIGITS  = 4         

data = [random.randint(1,9999) for _ in range(10)]
radix_sort(data)
print("Radix:", data)