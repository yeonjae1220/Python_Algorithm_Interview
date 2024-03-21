
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        def dfs(path, start):
            for i in range(start, len(nums)):
                if path and i <= nums.index(path[-1]):
                    return
                                
                path.append(nums[i])
                result.append(path[:])
                dfs(path, i + 1)
                path.pop()
            
        dfs([], 0)
        return result
        
nums = [4,1,0]
ans = Solution()
print(ans.subsets(nums))


