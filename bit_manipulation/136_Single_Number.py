from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

nums = [4,1,2,1,2]
print(Solution().singleNumber(nums))