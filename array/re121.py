"""
Runtime 790 ms Beats 20.36% of users with Python3 
Memory 27.55 MB Beats 11.19% of users with Python3
아니 왜 이게 생각이 안나지..
투포인터 비슷하게 left right 각 끝에서 내려오려고 하는데 생각보다 쉽지 않음
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy= 10000 # Constraints
        result = 0
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            result = max(result, prices[i] - buy)
        return result


# class Solution_failed:
#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) == 1:
#             return 0
        
#         result = 0
#         left, right = 0, len(prices) - 1
#         buy, sell = left, right
#         while buy < sell:
#             if prices[buy] > prices[left + 1]:
#                 left += 1
#                 buy = left
#                 continue
#             if prices[sell] < prices[right - 1]:
#                 right -= 1
#                 sell = right
#                 continue
#             while left < right and prices[left] < prices[buy] or prices[left] > prices[sell]:
#                 left += 1
            



            
            

        


# prices = [7,1,5,3,6,4]
# prices = [1,4,2]
# prices = [3,2,6,5,0,3]
print(Solution().maxProfit(prices))