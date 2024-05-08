from typing import List, Optional
from collections import deque
from type_converter import toLinkedList

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
"""
Runtime 294 ms Beats 47.10% of users with Python3 
Memory 37.96 MB Beats 7.03% of users with Python3
썩 좋은 방법은 아닌듯
"""


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        result = []
        while node:
            result.append(node.val)
            node = node.next
        
        return result[:] == result[::-1]
    

"""
deque가 빠르다 해서 함 돌려봄 -> 안빠름 그냥 리스트 인덱스 (pop() pop(0)) 와 비교해서 빠른거임
Runtime 305 ms Beats 29.93% of users with Python3 
36.54 MB Beats 55.46% of users with Python3
"""
class Solution_deque:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: deque = deque()

        #아래 if 문 없어도 통과 됨
        if not head:
            return True #아무 것도 없으면 True? 조건이 무조건 하나 이상 들어오는데
        

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True
    
"""
러너로 한번 풀어보기, 보자마자 그냥 리스트 슬라이스 냅다 박아서 이거 생각도 못했네
Runtime 298 ms Beats 40.12% of users with Python3 
Memory 37.65 MB Beats 8.72% of users with Python3
성능은 거기서 거긴데?
"""
class Solution_runner:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        half_list = []

        if not fast.next:
            return True

        while fast and fast.next:
            half_list.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        # 노드 개수 홀수일 경우 리스트에서 중간 남는 값 하나 넘겨주기
        if fast:
            slow = slow.next
        
        # 리스트 뒤집어 주기
        half_list[:] = half_list[::-1]
        
        for i in range(len(half_list)):
            if half_list[i] != slow.val:
                return False
            slow = slow.next
        return True

                
"""
Runtime 260 ms Beats 96.10% of users with Python3 
Memory 27.18 MB Beats 99.31% of users with Python3
pdf 나온대로 푸니까 약간 더 좋은듯? 리스트가 아니고 연결 리스트로 했어야 했나?
"""
class Solution_runner_pdf:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

# head = [1,2,2,1]
# head = [1,2]
# head = [1,0,0]
head = [1,0,1]
head_node = toLinkedList(head)
print(Solution_runner_pdf().isPalindrome(head_node))


