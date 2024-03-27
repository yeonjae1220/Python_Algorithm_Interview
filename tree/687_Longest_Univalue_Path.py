from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result: int = 0
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)

            #return left + right 이어져 있는 모든 간선 거미줄 처럼 세는게 아니네
            return max(left, right) #이렇게 쓰는것도 기억 해둬야 할듯. 구조상?
        dfs(root)
        return self.result
    
    #2트 실패, 거의 다왔는데;
    # longest: int = 0
    
    # def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
    #     def dfs(node: TreeNode, val: int) -> int:
    #         if not node:
    #             return 0
            
    #         left = dfs(node.left, node.val)
    #         right = dfs(node.right, node.val)

    #         if node.val == val:
    #             self.longest = max(self.longest, left + right + 1)
    #             return left + right + 1
    #         else:
    #             return 0

        
    #     dfs(root, root.val)
    #     return self.longest
            
        
        #1트 실패
        #     if not node.left and not node.right:
        #         return 0
            
        #     elif not node.right:
        #         return left
            
        #     left = dfs(node.left, node.val)
        #     right = dfs(node.right, node.val)

        #     if node.val == node.left.val == node.right.val:
        #         self.longest = max(self.longest, left + right + 1)
        #         return left + right + 1
        #     elif node.val == node.right.val:
        #         self.longest = max(self.longest, right + 1)
        #         return right + 1
        #     elif node.val == node.left.val:
        #         self.longest = max(self.longest, left + 1)
        #         return left + 1
        #     else:
        #         self.longest = max(self.longest, 1)
        #         return 1
            

        
        # dfs(root, root.val)
        # return self.longest
                



        
        




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

#root = [5,4,5,1,1,None,5]
#root = [1,4,5,4,4,None,5]
#root = [4,4,5,4,4,None,5]
node = createBinaryTree(root)
print(Solution().longestUnivaluePath(node))