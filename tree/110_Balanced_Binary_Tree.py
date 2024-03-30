#그냥 root 노드 받은거 레벨 순회 하면서 배열로 받고 배열 인덱스로 해결하는게 편해보이긴 함

from typing import Optional
import collections
import Tree_Visualizer
# from Tree_Visualizer import deserialize
# from Tree_Visualizer import preorder

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.check_result = True
        
        def height(node) -> int:
            # False가 확인될 때 재귀함수를 탈출하기 위해 작성
            # root = '[1,2,2,3,null,null,3,4,null,null,4]' 이 인풋일 때 아래 None값이 재귀 함수 내부로 전달되어서  TypeError: unsupported operand type(s) for -: 'int' and 'NoneType' 가 발생함
            # if self.check_result == False:
            #     return
            
            if node == None:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)

            #같은 레벨 노드의 높이 차가 2가 넘을 때 위에서 선언한 변수 값은 True -> False 변경
            if abs(left_height - right_height) >= 2:
                self.check_result = False
            
            return max(left_height, right_height) + 1
    
        height(root)
        return self.check_result

#pdf 풀이가 더 깔끔하다. 그리고 나의 코드는 False가 확인되어도 계속 계산을 하는 반면 pdf는 -1을 리턴하고 계속 이것이 리턴되어 빠르게 재귀를 탈출한다.
class Solution_pdf:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
        
            left = check(node.left)
            right = check(node.right)

            if left == -1 or right == -1 or abs(left-right) >= 2:
                return -1
            return max(left, right) + 1
        return check(root) != -1

# root = '[3,9,20,null,null,15,7]'
root = '[1,2,2,3,null,null,3,4,null,null,4]'
root_node = Tree_Visualizer.deserialize(root)
print(Solution().isBalanced(root_node))