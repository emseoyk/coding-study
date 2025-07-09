# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 1장 스택

#=========================================================
# 코드 1.1a: 스택을 위한 데이터
capacity = 10            # 스택 용량: 예) 용량을 10으로 지정
array = [None]*capacity  # 요소 배열: [None, ..., None] (길이가 capacity)
top = -1                 # 상단의 인덱스: 공백상태(-1)로 초기화 함

# 코드 1.1b: 스택의 공백상태와 포화상태 검사
def isEmpty( ) :
    if top == -1 : return True	# 공백이면 True 반환
    else : return False			# 아니면 False 반환

def isFull( ) : return top == capacity	# 비교 연산 결과를 바로 반환

# 코드 1.1c: 스택의 삽입 연산
def push( e ) :
    global top
    if not isFull() :		    # 포화상태가 아닌 경우
        top += 1			    # top 증가(global top 선언 필요)
        array[top] = e
    else :			            # 포화상태: overflow 
        print("stack overflow")
        exit()

# 코드 1.1d: 스택의 삭제 연산
def pop( ) :
    global top
    if not isEmpty():		    # 공백상태가 아닌 경우
        top -= 1			    # top 감소(global top 선언 필요)
        return array[top+1]
    else:			            # 공백상태: underflow 
        print("stack underflow")
        exit()

# 코드 1.1e: 스택의 peek() 연산
def peek( ) :
    if not isEmpty():		    # 공백상태가 아닌 경우
        return array[top]
    else: pass			        # underflow 예외는 처리하지 않았음

# 코드 1.1f: 스택의 size() 연산
def size( ) : return top+1	    # 현재 요소의 수는 top+1


#=========================================================
# 이 파일이 직접 실행될 때에는 다음 문장들을 실행함.
# 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음.
#=========================================================

if __name__ == "__main__":
    msg = input("문자열 입력: ")   # 문자열을 입력받음
    for c in msg :                # 문자열의 각 문자 c에 대해
        push(c)                   # c를 스택에 삽입

    print("문자열 출력: ", end='')
    while not isEmpty():          # 스택이 공백상태가 아니라면
        print(pop(), end='')      # 하나의 요소를 꺼내서 출력
    print()


