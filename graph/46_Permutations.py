#pdf 조금 봄
from typing import List
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        
        dfs(nums)
        return result

#use itertools module
class Solution_itertools:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

#input & check answer
ans = Solution()
nums = [1,2,3]
print(ans.permute(nums))
