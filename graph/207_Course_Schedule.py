#pdf 봄
#이해는 되는데 다시 한번 풀어봐야할듯
from typing import List 
import collections

class Solution_dfs:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        #require_for_end = [] 얘는 중복 값 갖지 않으므로 set() 사용
        require_for_end = set()
        def dfs(a):
            if a in require_for_end:
                return False
            
            require_for_end.add(a)
            for x in graph[a]:
                if not dfs(x):
                    return False
            require_for_end.remove(a)

            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True

            
class Solution_pruning:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        traced = set()
        visited = set()

        def dfs(i):
            #순환구조이면
            if i in traced:
                return False
            
            #이미 방문했던 노드이면
            if i in visited:
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            
            #탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            #탐색 종료 후 방문 노드 추가
            visited.add(i)

            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
            
        return True

numCourses = 2
prerequisites = [[1,0]]

print(Solution_pruning().canFinish(numCourses, prerequisites))