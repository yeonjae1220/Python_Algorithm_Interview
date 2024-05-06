"""
그냥 추가 저장공간 만들어서 left, right 곱한 값들 저장 해두고 빼 써보겠다
Runtime 280 ms Beats 14.89% of users with Python3 
Memory 26.44 MB Beats 6.66% of users with Python3
먼가..먼가 굳이 복잡하게 짠거 같음
pdf는 공간 복잡도 줄였다.
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult_left, mult_right = [nums[0]], [nums[-1]]
        result = []
        for i in range(1, len(nums) - 1):
            mult_left.append(mult_left[-1] * nums[i])
        for i in range(len(nums) - 2, 0, -1):
            mult_right.append(mult_right[-1] * nums[i])
        # 리스트 뒤집어 주기
        mult_right[:] = mult_right[::-1]
        result.append(mult_right[0])
        for i in range(len(nums) - 2):
            result.append(mult_left[i] * mult_right[i+1])
        result.append(mult_left[-1])

        return result


"""
이렇게 배열 하나를 초기화 해두고, for문 하나를 돌면서 pre, post를 left, right에서 곱해 오면서 
초기화 해둔 배열에다가 곱해주는 형식도 좋은듯. 더 깔끔하고 가시성이 좋아보인다.
"""
class Solution_leetcode:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)


nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))