from typing import List

# 음.. 왤케 못짰지
class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        left, right = 0, len(nums)
        if nums[0] == target:
            return 0
        
        while right-left > 1:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid
            else:
                right = mid
        
        return -1

#sol1 recursion
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left < right:
                mid = (left +right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binary_search(mid + 1, right)
                else:
                    return binary_search(left, mid - 1)
            else:
                return -1
            
        return binary_search(0, len(nums))
    
#sol2 loop, 내 풀이 깔끔한 버전
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


import bisect
#sol3 binary search module
class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
        # return nums[index]

#sol4 index solve that do not use binary search
class Solution4:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1

nums = [-1,0,3,5,9,12] 
target = 9
# nums = [-1,0,3,5,9,12] 
# target = 2
print(Solution4().search(nums, target))