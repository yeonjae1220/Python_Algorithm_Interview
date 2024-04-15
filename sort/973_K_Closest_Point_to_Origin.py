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
        


points = [[1,3],[-2,2]]
k = 1

print(Solution().kClosest(points, k))