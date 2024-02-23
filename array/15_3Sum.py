#loop entire couple of index, find appropriate value

#for문 중첩해서 하는 것보다 투포인터가 유리.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i]+ nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    #추가적인 triplets가 있는지 확인 해야함!
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        return result

nums = [-1,0,1,2,-1,-4]
ans = Solution()
print(ans.threeSum(nums))









#실패##########
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         triplets = []
#         for i in range(len(nums) - 1):
#             for j in range(i+1, len(nums)):
#                 temp_sum = nums[i] + nums[j]
#                 if temp_sum * -1 in nums and nums.index(temp_sum) != i and nums.index(temp_sum) != j:
#                     triplets.append(nums[i], nums[j], nums[nums.index(temp_sum - 1)])


# nums = [-1,0,1,2,-1,-4]
# answer = Solution()
# print(answer.threeSum(nums))

