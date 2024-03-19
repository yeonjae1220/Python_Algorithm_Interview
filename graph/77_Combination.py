#먼가 이상하게 안되서 pdf 봄
from typing import List
import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
                
        def dfs(elements, start: int, k: int):
            if k == 0:
                result.append(elements[:])
            
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
                
        dfs([], 1, k)
        return result
    

#use itertools module
class Solution_itertools:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))

ans = Solution()
n = 4 
k = 2
print(ans.combine(n, k))

        