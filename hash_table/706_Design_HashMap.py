#공부용으로 책보고 함, pdf 필기 참고
import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000 #set default size
        #collections.defaultdict -> It automatically generates a default when searching for a key
        #Be careful of bugs because it's handel automatic
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        #if there are no nodes, insert and terminate
        #인덱스가 없는것을 조회하면 자동으로 디폴트로 생성되기에 value로 비교
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        #if there exist nodes, deal with Linked List
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        #key search when node exist
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        
        #if first node in index, delete
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        #delete Linked List node
        #첫번째 노드일 경우 위에서 걸러짐, 
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)