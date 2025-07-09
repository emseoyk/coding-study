# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 2장 큐

#=========================================================
# 코드 2.1: 배열을 이용한 원형큐 클래스
#=========================================================

# 코드 2.1a: 원형 큐: 클래스 정의와 생성자
class ArrayQueue :
    def __init__( self, capacity = 10 ) :   # 생성자 정의
        self.capacity = capacity            # 용량(고정)
        self.array = [None] * capacity      # 요소들을 저장할 배열
        self.front = 0                     # 전단 인덱스
        self.rear = 0                      # 후단 인덱스

    # 코드 2.1b: 원형 큐: 공백상태와 포화상태 검사
    def isEmpty( self ) :                   # 공백 상태
        return self.front == self.rear

    def isFull( self ) :                    # 포화 상태
        return self.front == (self.rear+1)%self.capacity

    # 코드 2.1c: 원형 큐: 삽입 연산
    def enqueue( self, item ):              # 삽입 연산
        if not self.isFull():               # 포화 상태가 아닌 경우
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else : pass                         # 오버플로 오류: 처리 않음

    # 코드 2.1d: 원형 큐: 삭제 연산
    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else : pass                         # 언더플로 오류: 처리 않음

    # 코드 2.1e: 원형 큐: 상단 들여다보기 연산
    def peek( self ):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else : pass                         # 언더플로 오류: 처리 않음

    # 코드 2.1f: 원형 큐: 전체 요소의 수
    def size( self ) :
        return (self.rear - self.front + self.capacity) % self.capacity

    # 코드 2.1g: 원형 큐: 전체 요소를 화면으로 출력
    def display(self, msg='Queue:' ):
        print(msg, end='= [')
        count = self.size()
        for i in range(count):
            print(self.array[(self.front+1+i)%self.capacity], end=' ')
        print("]")


#=========================================================
# 코드 2.2: 원형 큐: 테스트 프로그램

import random
if __name__ == "__main__":
    q = ArrayQueue(8)               # 큐 객체를 생성(capacity=8)

    q.display("초기 상태")
    while not q.isFull() :          # 큐에 빈 칸인 남았으면
        q.enqueue(random.randint(0,100)) # 0~99사이의 정수 발생->삽입
    q.display("포화 상태")

    print("삭제 순서: ", end='') 
    while not q.isEmpty() :         # 큐에 요소가 남아 있으면
        print(q.dequeue(), end=' ') # 꺼내서 화면에 출력
    print()


