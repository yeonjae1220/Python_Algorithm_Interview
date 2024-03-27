from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#solution in leetcode(DevOgabek)
#res[0]안하고 res만 했을 땐 0 나옴 >> 참조를 이용하기 위해서(pdf 끝부분에도 나와있음)
#나중에 다시 봐야겠다 이 솔루션은
class Solution_leetcode_sol:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(node, res):
            if node is None:
                return 0
            left_depth = diameter(node.left, res)
            right_depth = diameter(node.right, res)

            #참조를 위해 이렇게 element 요소가 하나인 list를 사용함.
            res[0] = max(res[0], left_depth + right_depth)

            return max(left_depth, right_depth) + 1
        
        res = [0]
        diameter(root, res)

        return res[0]
        

#아이디어는 떠오르는데 구현이..
class Solution_pdf:
    longest: int = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            #왼쪽 오른쪽의 각 리프노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            #가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            #상태값
            return max(left, right) + 1
        
        dfs(root)
        return self.longest
        
        # left_depth = self.diameterOfBinaryTree(root.left)
        # right_depth = self.diameterOfBinaryTree(root.right)
        # return 1 + max(left_depth + right_depth)

#리스트를 받아서 이진트리를 만들어 주는 함수, 답 체크를 위해 따로 추가함
#왜 이게 잘 안만들어지냐; 만드는데 힘드너,,
# def list_to_node (val_list):
#     if val_list is None:
#         return None
    
#     root = TreeNode(val_list[0])
#     queue = collections.deque([root])

#     for val in val_list[1:]:
#         node = TreeNode(val)
#         if queue[-1].left is None:
#             queue[-1].left = node
#         else:
#             queue[-1].right = node
#             queue.pop()
#         queue.append(node)

#     return root

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



    
def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')



    
root = [1,2,3,4,5]
#node = list_to_node(root)
node = createBinaryTree(root)
# preorder(node)
# print("\n")
# inorder(node)
# print("\n")
# postorder(node)
    
print(Solution_pdf().diameterOfBinaryTree(node))
    