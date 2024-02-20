# len을 알아서 인덱스 끼리 반복문 돌리면서 직접 변경
# dequeue를 이용해서 위에 popleft()랑 pop이랑 쓰면서 위치 변경..?
# 슬라이싱 써서 [::-1] 로 바로 넣기?
# 그냥 reverse 써버리기


#solve 1 170ms 20.90MB 투 포인터를 이용한 스왑
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         left, right = 0, len(s) - 1
#         while(left < right):
#             s[left], s[right] = s[right], s[left] #파이썬에선 temp 같은 다른 변수 써도 되지만 이렇게도 가능!
#             left += 1
#             right -= 1


#solve 2 171ms 20.84MB 파이썬다운 방식
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         s = s.reverse()

#sovle 3
#s = s[::-1]
#원래 이것도 되지만 leetcode에서는 안된다. s[:] = s[::-1] 이렇게 하면 됨
#아마 공간 복잡도를 O(1) 으로 제한해서 그런거 같다고 함