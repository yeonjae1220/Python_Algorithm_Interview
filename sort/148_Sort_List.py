from typing import Optional
from typing import List
import converter_list2linkedlist

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#pdf 보고 함, mergesort
class Solution:
    #이쁘다 원리가
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2 # l1이 기본으로 return, l1이 null 일때 l2 리턴


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)

#quicksort는 timeout

#built-in fuction
class Solution3:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next

        list.sort()

        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head


head = [4,2,1,3]
input_head = converter_list2linkedlist.toLinkedList(head)
print(converter_list2linkedlist.printVal(Solution().sortList(input_head)))



        