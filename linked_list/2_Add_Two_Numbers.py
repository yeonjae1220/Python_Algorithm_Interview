#2 전가산기 구현
# from typing import List, Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         root = head = ListNode(0)

#         carry = 0
#         while l1 or l2 or carry:
#             sum = 0
#             if l1:
#                 sum += l1.val
#                 l1 = l1.next
#             if l2:
#                 sum += l2.val
#                 l2 = l2.next

#             carry, val = divmod(sum + carry, 10)
#             head.next = ListNode(val)
#             head = head.next

#         return root.next






"""
228, 229p 참고
"""
#문자열을 이용한 풀이
#Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
    
    def toList(self, node: ListNode) -> ListNode:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        
        return list
    
    def toReversedLinkedList(self, result: ListNode) ->ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        
        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
        int(''.join(str(e) for e in b))

        return self.toReversedLinkedList(str(resultStr))
        


# def makeNode(val: int) -> ListNode:
#     result: ListNode
#     result.val = val
#     result.next = None
#     return result

#leetcode에선 돌아가는데 여긴 list로 linkedlist에 집어넣으니 잘 안되서 그냥 리스트를 변환해서 집어넣음

def toLinkedList(list: List) ->ListNode:
    if not list:
        return None
    
    head = ListNode(list[0])
    current = head

    for value in list[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head
            


l1 = [6, 3, 1] 
l2 = [5,6,4]
ans_4_class = Solution()
ans = ans_4_class.addTwoNumbers(toLinkedList(l1), toLinkedList(l2))

while ans:
    print(ans.val)
    ans = ans.next

