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

#pdf, 깔끔하네 if문 이렇게 쓰니
class Solution:
    result = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.result += root.val
            root.val = self.result
            self.bstToGst(root.left)

        return root        

#음.. 왜 트리 순회가 보자마자 생각이 안났을까 (중위순회 뒤집어 둔거 (오른쪽 부터))
class Solution:
    result = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return 0
        self.bstToGst(root.right)
        self.result += root.val
        root.val = self.result
        self.bstToGst(root.left)

        return root

# 이러면 testcase에서 6 에서 5해서 5는 26이 들어가는데, 4 (root node) 할 때는 21 (6노드) 에서 4더해서 25가 나오게 됨
# class Solution:
#     def bstToGst(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return TreeNode(0) # 좋은 방법은 아닌거 같긴 한데, 리프노드 끝의 애들을 0을 가진 리프 노드를 덧붙여서 표현함, 아래 코드에 if문 넣어서 걸러도 괜찮았을듯?
        
#         root.val = root.val + self.bstToGst(root.right).val
#         print(root.val)
#         if root.left:
#             root.left.val = root.left.val + root.val
#             self.bstToGst(root.left)

#         return root
    
    
    

root = '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
# print(Tree_Visualizer.serialize(Solution().bstToGst(Tree_Visualizer.deserialize(root))))

root_node = Tree_Visualizer.deserialize(root)

result_node = Solution().bstToGst(root_node)

result = Tree_Visualizer.serialize(result_node)

print(result)
