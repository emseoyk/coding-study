# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 2장 큐


#=========================================================
# 코드 2.3: 링버퍼를 위한 원형큐 삽입 수정 및 테스트 프로그램 

class ArrayQueue :
    def __init__( self, capacity = 10 ) :   # 생성자 정의
        self.capacity = capacity            # 용량(고정)
        self.array = [None] * capacity      # 요소들을 저장할 배열
        self.front = 0                     # 전단 인덱스
        self.rear = 0                      # 후단 인덱스

    def isEmpty( self ) :                   # 공백 상태
       return self.front == self.rear

    def isFull( self ) :                    # 포화 상태
       return self.front == (self.rear+1)%self.capacity

    def enqueue( self, item ):              # 삽입 연산
        if not self.isFull():               # 포화 상태가 아닌 경우
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else : pass                         # 오버플로 오류: 처리 않음

    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else : pass                         # 언더플로 오류: 처리 않음

    def peek( self ):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else : pass                         # 언더플로 오류: 처리 않음

    def size( self ) :                      # 퀴즈
       return (self.rear - self.front + self.capacity) % self.capacity

    def display(self, msg='Queue:' ):
        print(msg, end='= [')
        count = self.size()
        for i in range(count):
            print(self.array[(self.front+1+i)%self.capacity], end=' ')
        print("]")

    # 코드 2.3a: 원형 큐: 링 버퍼를 위한 삽입 연산
    def enqueue2( self, item ):             # 링 버퍼 삽입 연산
        self.rear = (self.rear + 1) % self.capacity # 무조건 삽입
        self.array[self.rear] = item
        if self.isEmpty():                  # front == rear
            self.front = (self.front + 1) % self.capacity

#=========================================================
# 코드 2.3b: 링 버퍼의 테스트 프로그램

import random
if __name__ == "__main__":
    q = ArrayQueue(8)               # 큐 객체를 생성(capacity=8)

    q.display("초기 상태")
    for i in range(6) :             # enqueue2(): 0, 1, 2, 3, 4, 5
        q.enqueue2(i)
    q.display("삽입 0-5")

    q.enqueue2(6); q.enqueue2(7)    # enqueue2(): 6, 7
    q.display("삽입 6,7")

    q.enqueue2(8); q.enqueue2(9)    # enqueue2(): 8, 9
    q.display("삽입 8,9")

    q.dequeue(); q.dequeue()        # dequeue() 2회
    q.display("삭제  x2")


