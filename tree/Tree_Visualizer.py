# https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation
# https://leetcode.com/problems/recover-binary-search-tree/solutions/32539/Tree-Deserializer-and-Visualizer-for-Python/
import collections

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
    
def deserialize(string): # deserializatoin (역직렬화) : 직렬화된 파일 등을 역으로 직렬화하여 다시 객체의 형태로 만드는 것)
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def serialize(root) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = ['null'] #deserialize할 때 인덱스 편의를 위해 이렇게 index 0일 때 처리를 하는 듯
        queue = collections.deque()
        queue.append(root)

        while queue:            
            node = queue.popleft()
            # print(node.val)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append('null')
                    
        return ' '.join(result)

# def drawtree(root):
#     def height(root):
#         return 1 + max(height(root.left), height(root.right)) if root else -1
#     def jumpto(x, y):
#         t.penup()
#         t.goto(x, y)
#         t.pendown()
#     def draw(node, x, y, dx):
#         if node:
#             t.goto(x, y)
#             jumpto(x, y-20)
#             t.write(node.val, align='center', font=('Arial', 12, 'normal'))
#             draw(node.left, x-dx, y-60, dx/2)
#             jumpto(x, y-20)
#             draw(node.right, x+dx, y-60, dx/2)
#     import turtle
#     t = turtle.Turtle()
#     t.speed(0); turtle.delay(0)
#     h = height(root)
#     jumpto(0, 30*h)
#     draw(root, 0, 30*h, 40*h)
#     t.hideturtle()
#     turtle.mainloop()
    

#차곡차곡 이진트리 만들어 주는 함수
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

#트리 출력용
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

if __name__ == '__main__':
    preorder(deserialize('[1,2,3,null,null,4,null,null,5]'))
    # drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))