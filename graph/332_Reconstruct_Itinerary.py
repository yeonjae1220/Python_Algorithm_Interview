#pdf 보고 함
#보면 기초적인거 같은데 왜 안떠올랐지
from typing import List
import collections

class Solution_dfs:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []
        def dfs(a):
            while graph[a]: #if graph[a]: >>> tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]] 같은 입력 처리x
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        return route[::-1]


class Solution_loop:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]#tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
ans = Solution_dfs()
print(ans.findItinerary(tickets))