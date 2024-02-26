# Definition for singly-linked list.
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 반복문, prev 이해하는데 좀 걸림
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         root, prev = ListNode(None)
#         prev.next = head

#         while head and head.next:
#             a = head.next
#             head.next = a.next
#             a.next = head

#             prev.next = a

#             head = head.next
#             prev = prev.next.next
            
#         return root.next


#재귀        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            a = head.next
            head.next = self.swapPairs(a.next)
            a.next = head
            return a
        return head
        


def toLinkedList(list: List) ->ListNode:
    if not list:
        return None
    
    head = ListNode(list[0])
    current = head

    for value in list[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head

head = [1,2,3,4]
input = toLinkedList(head)
ans = Solution()
output = ans.swapPairs(input)

for i in range(len(head)):
    print(output.val)
    output = output.next

