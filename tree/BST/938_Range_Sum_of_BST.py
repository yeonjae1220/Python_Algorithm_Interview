import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from typing import Optional
from typing import List
import collections
import Tree_Visualizer

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = []
        def inorder(node) -> TreeNode:
            if node:
                node.left = inorder(node.left)
                if node.val >= low and node.val <= high:
                    result.append(node.val)
                node.right = inorder(node.right)
        
        inorder(root)
        return sum(result)

#재귀 구조 DFS로 브루트 포스 탐색
#내 풀이를 좀더 깔끔하게 풀이한것
class Solution_1:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        return (root.val if low <= root.val <= high else 0) + \
        self.rangeSumBST(root.left, low, high) + \
        self.rangeSumBST(root.right, low, high)
    
#DFS 가지치기로 필요한 노드 탐색
#막상 작성하려니 잘 안됬음, 그리고 내가 짠것보다 아래 pdf가 훨 깔끔함
class Solution_2:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode):
            if not root:
                return 0
            
            if root.val <= low:
                return dfs(root.right, low, high)
            elif root.val >= high:
                return dfs(root.left, low, high)
            # else:
            return node.val + dfs(node.left) + dfs(node.right)
        
        return dfs(root)
    
#반복 구조 DFS로 필요한 노드 탐색 (재귀 풀이를 반복으로)
# 등호 안넣는거 좋다
class Solution_3:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
            stack, sum = [root], 0
            while stack:
                node = stack.pop()
                if node.val > low: # 등호 안쓰는 이유가 어차피 low나 high와 같으면 제일 아래 if문에서 처리가 된다.
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
            return sum
    
#반복 구조 BFS로 필요한 노드 탐색
class Solution_4:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, sum = [root], 0
        while stack:
            node = stack.pop(0)
            if node.val > low:
                stack.append(node.left)
            if node.val < high:
                stack.append(node.right)
            if low <= node.val <= high:
                sum += node.val
        return sum



# root = '[10,5,15,3,7,null,18]'
# low = 7
# high = 15
    
root = '[10,5,15,3,7,13,18,1,null,6]'
low = 6
high = 10

root_node = Tree_Visualizer.deserialize(root)
print(Solution().rangeSumBST(root_node, low, high))