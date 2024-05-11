"""
219p 변수 스왑 원리에 관해서
"""

from typing import List, Optional
import type_converter
"""
prev만들어서 끝까지 밀어버려본다.
Runtime 36 ms Beats 66.48% of users with Python3 
Memory 17.80 MB Beats 34.05% of users with Python3
성능 별론데?
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev: ListNode = None
        while head:
            head, prev, prev.next = head.next, head, prev

        return prev
    
"""
pdf 풀이에 재귀 있어서 재귀로 한번 해봄
아니 왜이러지 재귀로 왜 안풀리냐, pdf보고 작성함
재귀로만 다시 풀어보기
"""
class Solution_recursive:
   def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)
        
        
        
       
                
        

head = [1,2,3,4,5]
head_node = type_converter.toLinkedList(head)
print(type_converter.toList(Solution_recursive().reverseList(head_node)))