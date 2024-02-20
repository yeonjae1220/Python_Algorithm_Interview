#투 포인터

# from typing import List

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0
        
#         volume = 0
#         left, right = 0, len(height) - 1
#         left_max, right_max = height[left], height[right]

#         while left < right:
#             left_max, right_max = max(height[left], left_max), max(height[right], right_max)

#             if left_max <= right_max:
#                 volume += left_max - height[left]
#                 left += 1
#             else:
#                 volume += right_max - height[right]
#                 right -= 1
            
#         return volume


# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# answer = Solution()
# print(answer.trap(height))



#stack
#stack[-1]은 제일 끝 요소를 가져옴

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                #스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break

                #이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume



height = [0,1,0,2,1,0,1,3,2,1,2,1]
answer = Solution()
print(answer.trap(height))


######################
#find start & end index of pattern decrease -> increase
#find h = min(height[i], height[j]) 
#and sum += min(height[i], height[j]) - height[indexs between i, j]
#아니다 그냥 책 봄


# height = [0,1,0,2,1,0,1,3,2,1,2,1]

# i, j = 0, 0

# #fine first water trap
# while height[i] <= height[i+1]:
#     i += 1

# j = i
# #fine decrease turning point
# while height[j] >= height[j+1]:
#     j += 1


# #fine increase turning point
# while height[j] <= height[j+1]:
#     j += 1




