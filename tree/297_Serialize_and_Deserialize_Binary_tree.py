from typing import Optional
import collections
from Tree_Visualizer import deserialize
from Tree_Visualizer import preorder

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

root = '[1,2,3,null,null,4,5]' # 입력을 이렇게 문자열로 받으면 아래 함수 적용 가능
preorder(deserialize(root))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))