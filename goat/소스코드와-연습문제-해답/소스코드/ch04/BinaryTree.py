# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 4장 트리


#=========================================================
# 코드 4.1: 이진트리를 위한 노드 클래스

class BTNode:
    def __init__ (self, elem, left=None, right=None):
        self.data = elem 
        self.left = left        # 왼쪽 자식을 위한 링크
        self.right = right      # 오른쪽 자식을 위한 링크

    def isLeaf(self):
        return self.left is None and self.right is None


# 코드 4.2: 이진트리의 전위순회
def preorder(n) :
    if n is not None :
        print('(', end=' ')     # 중첩된 괄호 표현을 위한 출력
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)
        print(')', end=' ')     # 중첩된 괄호 표현을 위한 출력

# 코드 4.3: 이진트리의 중위 순회
def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

# 코드 4.4: 이진트리의 후위 순회
def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')


# 코드 4.5: 이진트리의 레벨 순회
from queueCircular import CircularQueue
def levelorder(root) :
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)


# 코드 4.6: 이진트리의 노드의 개수 구하기
def count_node(n) :
    if n is None : 
        return 0
    else : 
        return 1 + count_node(n.left) + count_node(n.right)

# 코드 4.7: 이진트리의 높이 구하기
def calc_height(n) :
    if n is None : 
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

#=========================================================
# 코드 4.8: 이진트리 연산들의 테스트 프로그램
if __name__ == "__main__":
    d = BTNode('D', None, None)
    e = BTNode('E', None, None)
    b = BTNode('B', d, e)
    f = BTNode('F', None, None)
    c = BTNode('C', f, None)
    root = BTNode('A', b, c)

    print('\n   In-Order : ', end=''); inorder(root)
    print('\n  Pre-Order : ', end=''); preorder(root)
    print('\n Post-Order : ', end=''); postorder(root)
    print('\nLevel-Order : ', end=''); levelorder(root)
    print()

    print(" 노드의 개수 = %d개" % count_node(root))
    print(" 트리의 높이 = %d" % calc_height(root))