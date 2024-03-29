#애초에 내가 고민하고 있던 부분을 문제로 내주네
from typing import Optional
import collections
#from Tree_Visualizer import deserialize
from Tree_Visualizer import preorder
import Tree_Visualizer

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root) -> str:
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

    #이부분은 pdf 봄
    def deserialize(self, data) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if data == 'null null': # root로 #이 들어올 경우 예외 처리
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        #빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
        
        while queue:
            node = queue.popleft()
            if nodes[index] != 'null': #is not 쓰니 'null' 이 들어갔을 때 구문 오류가 계속 발생했었음. '#'일 때는 또 괜찮았음, 그냥 is not 대신 !=로 쓴다.
                print(nodes[index])
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] != 'null':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root

        

root = '[1,2,3,null,null,4,5]' # 입력을 이렇게 문자열로 받으면 아래 함수 적용 가능
#preorder(deserialize(root))
input_root = Tree_Visualizer.deserialize(root)


# ser = Codec().serialize(input_root)
# print(ser)
# #print(ser[1])
# nodes = ser.split()
# print(nodes[4])
# print(nodes[4] == 'null')
# if nodes[4] is not 'null':
#     print("ok")
# else:
#     print("error")


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(Tree_Visualizer.deserialize(root)))
preorder(ans)


# string = '# 1 2 3'
# print(string[2])