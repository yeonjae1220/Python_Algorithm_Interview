# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
from collections import deque
# from type_converter import toLinkedList
import type_converter

"""
Runtime 40 ms Beats 45.33% of users with Python3 
Memory 16.64 MB Beats 11.29% of users with Python3
음.. 겁나 별로네 성능이
head 노드 따로 만들어 놓고 list1, list2 노드들 돌면서 비교해서 집어넣었는데,, 흠..
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        node = head
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                node = node.next
                list1 = list1.next
            else:
                node.next = list2
                node = node.next
                list2 = list2.next
        
        if list1:
            node.next = list1
        else:
            node.next = list2

        return head.next

"""
재귀로 도전
이렇게 아얘 변수명을 바꿔버리면서 재귀로 돌리는거 아이디어 기억하놓기
Runtime 32 ms Beats 90.04% of users with Python3 
Memory 16.57 MB Beats 58.61% of users with Python3

pdf 답이 더 깔끔하다
"""
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val > list2.val:
            list1, list2 = list2, list1

        list1.next = self.mergeTwoLists(list1.next, list2)

        return list1


list1 = [1,2,4]
list2 = [1,3,4]
list1_node = type_converter.toLinkedList(list1)
list2_node = type_converter.toLinkedList(list2)
print(type_converter.toList(Solution2().mergeTwoLists(list1_node, list2_node)))