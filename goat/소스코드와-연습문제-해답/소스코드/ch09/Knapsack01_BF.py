# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 9장. 억지기법과 탐욕적 전략

#=========================================================
# 0-1 배낭 채우기
#=========================================================

# 코드 9.2: 0-1 배낭 채우기(억지 기법)

# wgt: 물건들의 무게 리스트
# val: 물건들의 가치 리스트
# W: 배낭의 용량
def Knapsack01_BF(wgt, val, W):
    n = len(wgt)
    bestVal = 0
    bestLst = []
    for i in range(2**n) :      # 0 ~ 2^n-1
#        print(".", end='')
        s = [0]*n
        for d in range(n) :
            s[d] = i%2
            i = i//2

        sumVal = 0
        sumWgt = 0
        for d in range(n):
            if s[d] == 1 :
               sumWgt += wgt[d]
               sumVal += val[d]

        if sumWgt <= W :
            if sumVal > bestVal :
                bestVal = sumVal
                bestLst = list(s)

    # print(bestVal, bestLst)
    return bestVal


# 0-1 배낭 채우기(억지 기법) 테스트 프로그램
if __name__ == '__main__':
    weight = [10, 20, 30, 25, 35]	# 물건별 무게
    value  = [60, 100, 120, 70, 85]	# 물건별 가치
    W = 80				            # 배낭의 제한 용량

    print("Knapsack01-BruteForce:", Knapsack01_BF(weight, value, W))
