"""
Runtime 339 ms Beats 39.90% of users with Python3 
Memory 17.62 MB Beats 56.17% of users with Python3
in의 시간 복잡도는 O(n) 전체 시간 복잡도는 O(n^2) 지만, in이 브루트 포스 보다 가볍고 빠르다.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            if target - nums[i] in nums[i+1:]:
                return [i, nums[i+1:].index(target - nums[i]) + i + 1]
            

"""
Runtime 62 ms Beats 54.58% of users with Python3 
Memory 17.85 MB Beats 16.24% of users with Python3
딕셔너리는 해시 테이블로 구성되어 있고, 조회는 평균적으로 O(1)에 가능 (최악은 O(n)), 전체는 O(n)
"""
class Solution_opt:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for index, num in enumerate(nums):
            if target - num in nums_map:
                return [index, nums_map[target-num]]
            else:
                nums_map[num] = index

        




nums = [2,7,11,15]
target = 9

print(Solution_opt().twoSum(nums, target))