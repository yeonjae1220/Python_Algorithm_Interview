from typing import List
# import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sort_sqrt = []
        result = []
        for i in range(len(points)):
            sort_sqrt.append([points[i][0] ** 2 + points[i][1] ** 2, i])
        
        sort_sqrt.sort()
        for i in range(k):
            result.append(points[sort_sqrt[i][1]])

        

        return result


# pdf sol, use heapq (priority queue)
class Solution_pdf:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result
        
"""
이는 파이썬의 heapq 모듈이 요소들을 튜플 형태로 관리하기 때문입니다. heapq 모듈은 리스트를 힙으로 취급하고, 이 힙은 순서를 기준으로 최소 힙(min heap)으로 동작합니다. 따라서 heapq 모듈을 사용하여 요소를 추가하거나 제거할 때 튜플을 사용하여 요소의 우선순위를 지정해야 합니다.
"""


points = [[1,3],[-2,2]]
k = 1

print(Solution().kClosest(points, k))