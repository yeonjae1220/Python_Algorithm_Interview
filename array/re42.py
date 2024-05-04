# stack 풀이 re
"""
Runtime 101 ms Beats 62.55% of users with Python3 
Memory 18.54 MB Beats 39.76% of users with Python3

제일 큰 기준 되는거 하나 잡아두고, 0, len(height) 각각 left & right 에서 오면서 계산
오 제일 인상 깊었던 문제라 그런지 한번에 풀었네 공부한 보람이 있다.
아니 근데 런타임이 pdf sol 대비 2배가 나오네

pdf에서는 left_max와 right_max를 따로 두고, while left < right:를 돌리며 while문 한번만 사용
그래서 나보다 런타임 1/2

어 pdf 투포인터 돌려보니 98ms 나옴. 흠... 하긴 while문이 2개일 뿐이지 실제로 탐색하는 횟수는 거의 동일하네
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0        
        left, right = 0, len(height) - 1
        h = max(height)
        h_idx = height.index(h)

        temp = 0
        while left < h_idx:
            if height[left] > temp:
                temp = height[left]
            
            if height[left] < temp:
                result += temp - height[left]
                
            left += 1

        temp = 0
        while right > h_idx:
            if height[right] > temp:
                temp = height[right]
            
            if height[right] < temp:
                result += temp - height[right]
                
            right -= 1

        return result
        
"""
stack 풀이 방법 기억 안나서 pdf로 복습하고 재도전
Runtime 105 ms Beats 48.75% of users with Python3 
Memory 18.39 MB Beats 92.09% of users with Python3
왜 얘도 2배 나오냐

"""
class Solution_stack:
    def trap(self, height: List[int]) -> int:
        stack = []
        volumn = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not stack:
                    break

                distance = i - stack[-1] - 1
                water = min(height[i], height[stack[-1]]) - height[top]
                volumn += distance * water
            
            stack.append(i)
        return volumn


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution_stack().trap(height))
# ans = 6