from typing import List
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1
        
#try to use binary search
#최소값 넣어서 찾는 bisect 처럼 해도 될꺼 같긴 한데 논리적으로 풀고 싶다
#failed
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return target
            else:
                return -1
        
        left, right = 0, len(nums) - 1
        pivot = 0

        # pivot 구하기
        while left < right:
            mid = left + (right - left) // 2

            if nums[right] < nums[left] < nums[mid]:
                left = mid
            else:
                right = mid


        
        pivot = left + 1

        nums = nums[pivot:] + nums[:pivot]
        
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index + pivot
        else:
            return -1

            
#pdf
#복습할 때 꼮 다시 풀어 보자.. 갑자기 지능 떨어진 느낌
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        #예외처리
        if not nums:
            return -1
        
        #최솟값을 찾아 피벗 설정
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]: # 이렇게 하니 되네.. 
                left = mid + 1
            else:
                right = mid

        pivot = left

        #피벗 기준 이진 탐색
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1            
"""
1 2 3 4 5

2 3 4 5 1

3 4 5 1 2

4 5 1 2 3

6 7 1 2 3 4 5

5 1 2 3 4

"""

nums = [4,5,6,7,0,1,2]
target = 0

# nums = [4,5,6,7,0,1,2]
# target = 3

print(Solution().search(nums, target))
