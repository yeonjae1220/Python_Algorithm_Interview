from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
    
nums = [1,4,3,2]
ans = Solution()
print(ans.arrayPairSum(nums))
