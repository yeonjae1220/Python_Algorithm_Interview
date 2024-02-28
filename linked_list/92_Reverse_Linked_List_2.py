from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#flipping node with iterative structure
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head or left == right:
            return head
        #예외가 발생했습니다. TypeError
        # cannot unpack non-iterable ListNode object
        #root, start = ListNode(None)
        #root.next = head #이러면 start.next 도 head?
        # 아 아  root = start = Listnode(None) 하면 됨
        
        #다중할당 동일한 참조
        #이렇게 하면 에러
        # root = ListNode(None) 
        # start = ListNode(None)

        #이렇게 하면 동작
        root = start = ListNode(None)

        root.next = head

        #print(start.next.val) => 3

        for _ in range(left-1):
            start = start.next
        end = start.next
        #print(start.next.val, root.next.val)

        for _ in range(right - left):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp
        
        return root.next



#solve with convert linkedlist to list and use slicing
class Solution_2:
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
        

head = [1, 2, 3, 4, 5] 
left = 2
right = 4

ans = Solution()
result = ans.reverseBetween(toLinkedList(head), left, right)
# for i in range (len(head)):
#     print(result.val)
#     result = result.next



list_a = [1, 2, 3, 4, 5]
a = toLinkedList(list_a)
b = c = ListNode(None)

#같은 None으로 할당한 새로운 노드를 참조 했기에, b.next했을때 해당 Node의 next가 
#a로 변했기에, c도 마찬가지가 된다.
b.next = a
print(b.next.val, c.next.val)
#>>>1 1
print(id(b), id(c))
#>>>4329474896 4329474896 같은 id

#얘는 다른 node를 받아서 아예 새로운 참조를 하는 것인듯 하다.
b = b.next
print(b.next.val, c.next.val)
#2 1
print(id(b), id(c))
#4329475856 4329474896 다른 id