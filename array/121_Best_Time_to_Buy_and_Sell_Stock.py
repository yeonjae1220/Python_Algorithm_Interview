#썩 좋은 풀이는 아니다. 최대값들을 배열 역순으로 넣어두고, 다시 처음부터 돌면서 
#최소 최댓값 차 max 찾는걸로 했었음
# from typing import List
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         highest_price = [0]
#         result = 0
#         for i in range(len(prices) - 1, 0, -1):
#             highest_price.append(max(highest_price[-1], prices[i]))
#         for i in range(len(prices)):
#             result = max(result, highest_price[len(prices) - i -1] - prices[i])
#         return result


#책에서 나온 방법으로 위에 849ms가 789ms가 됨..? 크게 차이 없는데?
from typing import List
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_pirce = sys.maxsize #들어갈 수 있는 최댓값 (정수형 최댓값))

        for price in prices:
            min_pirce = min(min_pirce, price)
            profit = max(profit, price - min_pirce)

        return profit

prices = [7,6,4,3,1]
ans = Solution()
print(ans.maxProfit(prices))