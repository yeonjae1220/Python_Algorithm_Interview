"""
Runtime 199 ms Beats 99.30% of users with Python3 
Memory 20.02 MB Beats 9.24% of users with Python3
오 파이썬다운 풀이 pdf랑 똑같이 품
"""
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


nums = [1,4,3,2]
print(Solution().arrayPairSum(nums))