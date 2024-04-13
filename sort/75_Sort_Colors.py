from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:# None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1
            i += 1

        return nums
    
#Dutch National Flag Problem
class Solution_pdf:
    def sortColors(self, nums: List[int]) -> List[int]:# None:
        # red, white, blue = 0, 0, len(nums)

        # while white < blue:
        #     if 

        i, j, k = 0, 0, len(nums)
        while j < k:
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]
            else:
                j +=1
        
        return nums
    
nums = [2,0,2,1,1,0]
print(Solution_pdf().sortColors(nums))
        