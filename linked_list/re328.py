from typing import Optional, List
import type_converter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
사람이 어째 시간이 지나고 퇴화한거 같냐
Runtime 41 ms Beats 49.18% of users with Python3 
Memory 18.54 MB Beats 70.18% of users with Python3
"""

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # odd, even = head, head.next
        # even_head = head.next
    
        odd = odd_head = ListNode(None)
        even = even_head = ListNode(None)

        while head and head.next:
            odd.next = head
            odd = odd.next

            even.next = head.next
            even = even.next
            
            head = head.next.next

        if head:
            odd.next = head
            odd = odd.next
        
        even.next = None

        odd.next = even_head.next

        return odd_head.next

        


head = [2,1,3,5,6,4,7]
input = type_converter.toLinkedList(head)
print(type_converter.toList(Solution().oddEvenList(input)))
