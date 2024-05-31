# Definition for singly-linked list.
from typing import Optional, List
import type_converter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
재귀 다시 풀어보기
"""
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            temp = head.next
            head.next = self.swapPairs(temp.next)
            temp.next = head
            return temp
        return head

        


"""
반복 다시 풀어보기
생각보다 삽질을 많이 하는데 다시 풀어보는게 좋을 것 같다.
"""

class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode()
        
        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = head

            prev.next = temp
            
            # head.next = head.next.next
            # head.next.next = head

            # prev.next = 

            prev = prev.next.next
            head = head.next
            

        
        return root.next
    

head = [1,2,3,4]
input = type_converter.toLinkedList(head)
print(type_converter.toList(Solution().swapPairs(input)))

        
