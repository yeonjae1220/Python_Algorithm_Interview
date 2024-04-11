from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def toLinkedList(list: List) ->ListNode:
    if not list:
        return None
    
    head = ListNode(list[0])
    current = head

    for value in list[1:]:
        current.next = ListNode(value)
        current = current.next
    
    
    return head


def tolist(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def printVal(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result