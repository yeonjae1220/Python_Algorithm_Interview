#I resovle this problem, but I solve it almost memorize last produced answer
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        
        return answer



temperatures = [73,74,75,71,69,72,76,73]
ans = Solution()
print(ans.dailyTemperatures(temperatures))


# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = [0] * len(temperatures)
#         stack = []
#         for i, cur in enumerate(temperatures):
#             while stack and cur > temperatures[stack[-1]]:
#                 last = stack.pop()
#                 answer[last] = i - last
#             stack.append(i)

#         return answer