from typing import List, Optional
import type_converter

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
실패함, carry가 끝에 안붙어, 왜?
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = l1
        while l1 and l2:
            sum = l1.val + l2.val + carry
            val, carry = sum % 10, sum // 10
            l1.val = val
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum = l1.val + carry
            val, carry = sum % 10, sum // 10
            l1.val = val
            l1 = l1.next
            
        while l2:
            sum = l2.val + carry
            val, carry = sum % 10, sum // 10
            l2.val = val
            l1 = l2
            l1 = l1.next
            l2 = l2.next
        
        if carry:
            l1 = ListNode(carry)
        
        return result
    

"""
다시
"""
class Solution_re:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        result = head
        carry = 0

        while l1 or l2 or carry:
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            carry, val = divmod(sum_val, 10)
            result.next = ListNode(val)
            result = result.next

        return head.next
                

            


"""
그래 이걸 하고 싶었는데 왜 이게 안되냐
Runtime 59 ms Beats 32.04% of users with Python3 
Memory 16.60 MB Beats 90.34% of users with Python3
"""
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()  # 결과 리스트의 더미 노드 생성
        result = dummy  # 결과 리스트의 시작을 dummy로 설정

        while l1 or l2 or carry:
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next

            carry, val = divmod(sum_val, 10)
            result.next = ListNode(val)  # 결과 리스트에 노드 추가
            result = result.next

        return dummy.next  # 더미 노드 다음부터가 실제 결과 리스트


# l1 = [2,4,3]
# l2 = [5,6,4]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
l1 = type_converter.toLinkedList(l1)
l2 = type_converter.toLinkedList(l2)
print(type_converter.toList(Solution_re().addTwoNumbers(l1, l2)))
