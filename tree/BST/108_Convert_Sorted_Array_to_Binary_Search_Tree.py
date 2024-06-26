#pdf 봄
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from typing import Optional
from typing import List
import collections
import Tree_Visualizer
# from tree.Tree_Visualizer import preorder, deserialize
# from .. import Tree_Visualizer
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2

        #분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node
    
nums = [-10,-3,0,5,9]
root = Solution().sortedArrayToBST(nums)
Tree_Visualizer.preorder(root)
