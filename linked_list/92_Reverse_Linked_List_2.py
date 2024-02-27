from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#solve with convert linkedlist to list and use slicing
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #convert linked list to list
        def toList(node: Optional[ListNode]):
            list: List = []
            while node:
                list.append(node.val)
                node = node.next
            return list
        
        list: List = toList(head)
        reversed_list = list[0:left-1] + list[left - 1:right][::-1] + list[right:]
        #list[left - 1:right:-1] 이렇게 하나로 슬라이싱 하니 안된다.
        #>>>아 앞에 start end 를 바꿔 써줘야함
        #list[right - 1:left - 2:-1] 이렇게 하니 input = [5] 일 때 output이 안나옴
        #예외 처리 해줘야한다.
        #print(reversed_list)
        


        #convert list to linked list (switch, change, convert)
        def toLinkedList(list: List) ->ListNode:
            if not list:
                return None
            
            head = ListNode(list[0])
            current = head

            for value in list[1:]:
                current.next = ListNode(value)
                current = current.next
            
            return head
        
        return toLinkedList(reversed_list)




def toLinkedList(list: List) ->ListNode:
    if not list:
        return None
    
    head = ListNode(list[0])
    current = head

    for value in list[1:]:
        current.next = ListNode(value)
        current = current.next
    
    
    return head
        

head = [1,2,3,4,5] 
left = 2
right = 4

ans = Solution()
result = ans.reverseBetween(toLinkedList(head), left, right)
for i in range (len(head)):
    print(result.val)
    result = result.next

