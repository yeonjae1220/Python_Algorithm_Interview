#공부용으로 책보고 함, pdf 필기 참고
#힙 참고 자료
#https://littlefoxdiary.tistory.com/3
#https://wikidocs.net/194445
from typing import Optional, List
import heapq 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            #save root of each linked linst in heap
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i])) #중복된 값 구분할 수 있게 추가적인 정보를 넣음
            
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        
        return root.next


#답 확인용 입력 자료형 변환 함수
def toLinkedList(list: List) ->ListNode:
    if not list:
        return None
    
    head = ListNode(list[0])
    current = head

    for value in list[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head

ans = Solution()
# lists = [[1,4,5],[1,3,4],[2,6]]
list_a = [1,4,5]
list_b = [1,3,4]
list_c = [2,6]
lists = [toLinkedList(list_a), toLinkedList(list_b), toLinkedList(list_c)]
#temp = ListNode(lists)

fin = ans.mergeKLists(lists)
while fin:
    print(fin.val)
    fin = fin.next