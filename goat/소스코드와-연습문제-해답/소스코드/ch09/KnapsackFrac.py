# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 9장. 억지기법과 탐욕적 전략

#=========================================================
# 분할 가능한 배낭 채우기
#=========================================================

# 코드 9.3: 분할 가능한 배낭 채우기(탐욕적 기법)
def KnapSackFrac(wgt, val, W):
    bestVal = 0                 # 전체 배낭의 가치
    for i in range(len(wgt)):
        if W <= 0 :             # 용량이 다 찬 경우
           break
        if W >= wgt[i]:         # 물건 전체가 들어갈 수 있는 경우
            W -= wgt[i]
            bestVal += val[i] 
        else:                   # 물건의 일부만 넣을 수 있는 경우
            fraction = W / wgt[i]
            bestVal += val[i] * fraction 
            break

    return bestVal

weight = [12,  10, 8]	# 물건별 무게 (가치/무게 의 내림차순으로 정렬됨)
value  = [120, 80, 60]	# 물건별 가치 (가치/무게 의 내림차순으로 정렬됨)
W = 18				    # 배낭의 제한 용량
print("Fractional Knapsack(18):", KnapSackFrac(weight, value, W)) 
