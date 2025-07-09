# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 2장 큐


#=========================================================
# 코드 2.4: 원형 큐를 상속한 원형 덱 클래스

from ArrayQueue import *

# 코드 2.4a: 원형 덱: 큐를 상속한 클래스 정의
class CircularDeque(ArrayQueue) :
    def __init__( self, capacity=10 ) :
        super().__init__(capacity)

    # 코드 2.4b: 원형 덱: 동작이 동일한 연산들
    def addRear( self, item ): self.enqueue(item )
    def deleteFront( self ): return self.dequeue()
    def getFront( self ): return self.peek()

    # 코드 2.4c: 원형 덱: 추가된 연산들
    def addFront( self, item ):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else: pass

    def deleteRear( self ):
        if not self.isEmpty():
            item = self.array[self.rear];
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item
        else: pass

    def getRear( self ): 
        if not self.isEmpty():
            return self.array[self.rear]
        else: pass


#=========================================================
# 코드 2.5: 원형 덱: 테스트 프로그램

if __name__ == "__main__":
    dq = CircularDeque()

    for i in range(9):
        if i%2==0 : dq.addRear(i)
        else : dq.addFront(i)
    dq.display("홀수는 전단 짝수는 후단 삽입")

    for i in range(2): dq.deleteFront()
    for i in range(3): dq.deleteRear()
    dq.display("전단 삭제 2번, 후단 삭제 3번")

    for i in range(9,14): dq.addFront(i)
    dq.display("전단에 9 ~ 13 삽입")
