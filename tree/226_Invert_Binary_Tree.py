
from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = collections.deque()

        queue.append(root)

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
            
# pythonic way
#진짜 야무지게 짜놨네 이쁘다
class Solution_pythonic_way:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None #이 줄은 없어도 된다.


# BFS with loop structure
#내가 한 풀이와 유사 근데 더 깔끔
class Solution_BFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)# 어차피 None이라도 위에 while 조건문에서 걸러져서 괜찮네            
                queue.append(node.right)
        return root
    
# DFS with loop structure
#위 풀이와 유사
class Solution_DFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()

            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)# 어차피 None이라도 위에 while 조건문에서 걸러져서 괜찮네            
                stack.append(node.right)
        return root

# post-order DFS with loop structure
class Solution_DFS_post_order:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()

            if node:
                stack.append(node.left)
                stack.append(node.right)
                node.left, node.right = node.right, node.left #post order
        return root



def insertLevelOrder(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root

def createBinaryTree(arr):
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    return root

#레벨별 이진트리 순회 출력 함수
def level_order_traversal(root):
    if root is None:
        return
    
    # 큐를 이용하여 레벨별로 노드를 순회
    queue = [root]
    
    while queue:
        # 현재 레벨의 노드 개수
        level_length = len(queue)
        
        for _ in range(level_length):
            # 큐에서 노드를 꺼내서 값 출력
            node = queue.pop(0)
            print(node.val, end=" ")
            
            # 노드의 자식 노드를 큐에 추가
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

root = [4,2,7,1,3,6,9]
make_root_node = createBinaryTree(root)
root_node = Solution_pythonic_way().invertTree(make_root_node)
level_order_traversal(root_node)

