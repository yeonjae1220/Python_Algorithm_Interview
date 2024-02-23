#어우 재귀 생각해보면 단순한데 이해할려고 엄청 봤네
#다음에 재귀로 다시 풀어보기! 
#그냥 따지고 보면 제일 작은 애 찾아 가면서 다른 리스트에 핑 찍어두고 움직이는 거랑 다를게 없긴함
#근데 그냥 각각 linked list 진행시켜가며 푸는게 머리는 편할듯

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
from collections import deque

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1