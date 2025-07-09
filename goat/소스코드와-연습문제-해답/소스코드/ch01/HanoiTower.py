# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 1장 스택

#=========================================================
# 코드 1.9: 하노이의 탑

def hanoi_tower(n, fr, tmp, to) :
    if (n == 1) :				                # 종료 조건
        print("원판 1: %s --> %s" % (fr, to))	# 하나의 원판 이동
    else :
        hanoi_tower(n - 1, fr, to, tmp)		    # 단계 ➊
        print("원판 %d: %s --> %s" % (n,fr,to))	# 단계 ➋
        hanoi_tower(n - 1, tmp, fr, to)		    # 단계 ➌



# 테스트 프로그램
step = 1
hanoi_tower(4, 'A', 'B', 'C')


