#다른 순회 조합들로도 문제 풀어보기
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            # preorder result is divide index of inorder
            index = inorder.index(preorder.pop(0))

            #DP of inorder result
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])
        
            return node
        

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(Tree_Visualizer.serialize(Solution().buildTree(preorder, inorder)))