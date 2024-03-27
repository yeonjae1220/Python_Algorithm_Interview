# Definition for a binary tree node.

from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        #그냥 리스트 입력인거 같아서 2^n 계산으로 높이 계산할려 했는데 input type이 list가 아니라고 해서 len을 못쓴다네요
        # if not root:
        #     return 0
        
        # num_node = len(root)
        # result = 1
        # while num_node > 1:
        #     num_node //= 2
        #     result += 1
        
        # return result
        
        #타입 맞추기 묘하네, 트리 탐색하면서 모든 노드 방문해서 cnt로 node 개수 count함
        # cnt = 0
        # def find_depth(node):
        #     if not node:
        #         return
        #     find_depth(node.left)
        #     cnt += 1        
        #     find_depth(node.right)
        #     cnt += 1
        
        # find_depth(root)
        # result = 1
        # while cnt > 1:
        #     cnt //= 2
        #     result += 1

        # return result

        #pdf 풀이 (bfs)
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        

        return depth


root = [1,None,2]#[3,9,20,None,None,15,7]
print(Solution().maxDepth(root))


#leetcode solution 1
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)