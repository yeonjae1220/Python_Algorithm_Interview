from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul_left, mul_right, result = [1], [1], []
        for i in range(0, len(nums) - 1):
            mul_left.append(mul_left[-1] * nums[i])
        for i in range(len(nums) - 1, -1, -1): #reverse 함수도 사용 가능
            mul_right.append(mul_right[-1] * nums[i])
        for i in range(len(nums)):
            result.append(mul_left[i] * mul_right[len(nums) - 1 - i])
    
        return result




nums = [1,2,3,4]
ans = Solution()
print(ans.productExceptSelf(nums))

# for i in range(4, 0, -1):
#     print(i)