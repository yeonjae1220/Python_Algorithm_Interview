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

# 솔직히 그냥 리스트 넣어서 정렬하면 편할텐데 (아님)
# 와 진짜 딱 중위순회였네 bst에서 오름차순 혹은 내림차순으로 순회할 수 있다
class Solution1:
    prev = -sys.maxsize
    result = 100001
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result
        #  left = self.minDiffInBST(root.left)
        # self.result_min = min(self.result_min, )

#반복 구조로 중위 순회
#오히려 얘가 더 익숙하질 않아서 어렵게 느껴짐
class Solution1:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result


#반복 복습
class Solution1_1:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop() #
            result = (result, node.val - prev)
            prev = node.val

            node = node.right

        return result

        

#자식 노드 사이의 차의 최솟값을 구하는 코드, 문제 이해를 약간 잘못함. (코드도 맘에 안듬, 주어진 조건 <= 10^5 쓰는것도 뭔가 불쾌함)
#자식 끼리만 구할게 아니고 다른 밀접한 노드 사이의 관계도 생각 해야한다.
class Solution_failed:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:        
        #root.left가 null 이 아닐때, root.val - root.left.val
        #root.right가 null 이 아닐때, root.right.val - root.val
        #위 두 값과 현재까지의 min값 비교해서 min값 return
        if not root:
            return 100001
        min_dif = 100001
        if root.left:
            min_dif = min(min_dif, root.val - root.left.val)
        if root.right:
            min_dif = min(min_dif, root.right.val - root.val)
        
        return min(min_dif, self.minDiffInBST(root.left), self.minDiffInBST(root.right))
    



# root = '[4,2,6,1,3]'
# root = '[1,0,48,null,null,12,49]'
root = '[90,69,null,49,89,null,52]'
root_node = Tree_Visualizer.deserialize(root)
print(Solution().minDiffInBST(root_node))