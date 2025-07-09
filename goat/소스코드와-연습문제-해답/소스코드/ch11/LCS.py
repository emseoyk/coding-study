# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 11장. 동적 계획법

#=========================================================
# 최장 공통 부분 순서(LCS)
#=========================================================

# 코드 11.3: LCS의 길이(분할 정복)
def lcs_recur(X, Y, m, n): 
    if m == 0 or n == 0: 			# base case 
        return 0 
    elif X[m-1] == Y[n-1]: 		# case 1: x_m == y_n
        return 1 + lcs_recur(X, Y, m-1, n-1) 
    else: 						# case 2
        return max(lcs_recur(X, Y, m, n-1), lcs_recur(X, Y, m-1, n)) 



# 코드 11.4: LCS의 길이(동적 계획법)
def lcs_dp(X , Y): 
    m = len(X) 
    n = len(Y) 
    L = [[None]*(n+1) for _ in range(m+1)] 	# 테이블 생성
  
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 :		# base case: 하나의 길이라도 0이면
                L[i][j] = 0			# LCS --> 0
            elif X[i-1] == Y[j-1]:	# 마지막 글자가 같으면
                L[i][j] = L[i-1][j-1]+1
            else:					# 마지막 글자가 다르면
                L[i][j] = max(L[i-1][j], L[i][j-1])

    for i in range(m+1):
        print(L[i])
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    print("LCS = ", lcs_dp_traceback(X, Y, L))

    return L[m][n] 



# 코드 11.5: LCS 테이블에서 LCS를 추적하는 알고리즘
def lcs_dp_traceback(X, Y, L):
    lcs = ""													# ①
    i = len(X)													# ②
    j = len(Y)													# ② 
    while i > 0 and j > 0:
        v = L[i][j] 
        if v > L[i][j-1] and v > L[i-1][j]  and v > L[i-1][j-1]:# ③
            i -= 1
            j -= 1
            lcs = X[i] + lcs

        elif v == L[i][j-1] and v > L[i-1][j]: j -= 1			# ④
        else : i -= 1											# ⑤

    return lcs


# 코드 11.6: LCS 테스트 프로그램
X = "GAME OVER"
Y = "HELLO WORLD"
print("X = ", X)
print("Y = ", Y)
print("LCS(분할 정복)", lcs_recur(X , Y, len(X), len(Y)))
print("LCS(동적 계획)", lcs_dp(X , Y) )


X = "ABCDGH"
Y = "AEDFHR"
print("LCS(동적 계획)", lcs_dp(X , Y) )

X = "AGGTAB"
Y = "GXTXAYB"
print("LCS(동적 계획)", lcs_dp(X , Y) )
