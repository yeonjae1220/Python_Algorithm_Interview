from typing import Optional
import converter_list2linkedlist

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#pdf 봄
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            # 최적화
            if head and cur.val > head.val:
                cur = parent 

        return parent.next

head = [4,2,1,3]
head_node = converter_list2linkedlist.toLinkedList(head)

print(converter_list2linkedlist.printVal(Solution().insertionSortList(head_node)))
