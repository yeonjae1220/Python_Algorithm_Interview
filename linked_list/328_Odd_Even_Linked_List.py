from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#책 풀이
# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
#         odd, even = head, head.next
#         even_root = even
        
#         while even and even.next:
#             odd.next = odd.next.next
#             odd = odd.next
#             even.next = even.next.next
#             even = even.next
        
#         odd.next = even_root
#         return head



## 테스트 케이스 반밖에 못넘김 Error - Found cycle in the ListNode 라는데?
#어째서..?
#even 마지막 노드 None 설정 안해서 그런듯
#그래도 코드가 더럽긴 하다
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(None)
        even = ListNode(None)
        root_odd, root_even = odd, even

        while head:
            odd.next = head
            odd, head = odd.next, head.next
            
            if head:
                even.next = head
                even, head = even.next, head.next
        
        # 마지막 노드 다음을 None으로 설정
        odd.next = None
        even.next = None

        odd.next = root_even.next
        return root_odd.next



def toLinkedList(list: List) ->ListNode:
    if not list:
        return None
    
    head = ListNode(list[0])
    current = head

    for value in list[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head

head = [2,1,3,5,6,4,7]
input = toLinkedList(head)
ans = Solution()
output = ans.oddEvenList(input)

for i in range(len(head)):
    print(output.val)
    output = output.next
