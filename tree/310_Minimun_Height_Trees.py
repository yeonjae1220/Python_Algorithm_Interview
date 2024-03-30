from typing import Optional
from typing import List
import collections
import Tree_Visualizer

class Solution_pdf:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        #첫 번째 리프노드 추가
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)

        #루트 노드만 남을 때 까지 반복 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                # 리프노드와 붙어있단 (다음 리프노드 후보) 애들 제거, 다음 리프노드와 현재 리프노드 연결 제거
                neigbor = graph[leaf].pop()
                graph[neigbor].remove(leaf)

                if len(graph[neigbor]) == 1:
                    new_leaves.append(neigbor)

            leaves = new_leaves

        return leaves


#아이디어 pdf에서 단계별 리프노드 제거를 봐버림 어라 근데 어쨰서? 암튼 아래는 실패임
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        
        if edges == [] and n == 1:
            return [0]
        
        if n == 2:
            return edges[0]

        
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        result = []
        for i in range(n):
            result.append(i)


        for i in graph:
            if len(graph[i]) == 1:
                result.remove(i)
                for j in graph:
                    if i in graph[j]:
                        graph[j].remove(i)

        return result

# n = 4
# edges = [[1,0],[1,2],[1,3]]
# n = 6
# edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# n = 1
# edges = []
# n = 2
# edges = [[0,1]]
n = 6
edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]
print(Solution_pdf().findMinHeightTrees(n, edges))