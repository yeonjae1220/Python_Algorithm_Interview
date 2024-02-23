from typing import List, Optional
# https://www.daleseo.com/python-typing/
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
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
        # for i in range(len(q) / 2):
        #     if q[i] != q[len(q) - i]:
        #         return False
        # return True
            

###############
#파이썬 다중 할당 중, 파이썬의 중요한 특징!
# a = [1, 2, 3]
# print(id(a))
# b = [4, 5]
# print(id(b))

# b = a

# b.append(6)

# print(a)
