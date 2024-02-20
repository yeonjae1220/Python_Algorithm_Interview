
#solve 1. Runtime 215ms Memory 22.45MB 
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = []
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())

#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False
        
    
#         return True
        

#solve 2. Runtime 56ms Memory 21.92MB
#deque란 collections 모듈에 속해있다.
#strs: Deque = collecitons.deque() 이렇게 하니까 여기선 에러 보여서 아래처럼 함
# from collections import deque

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = deque()

#         print("input strings : ")
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())

#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return print ("False")
        
    
#         return print("True")
        
#solve 3 Runtime 32ms Memory 18.14MB
#정규 표현식을 활용할 땐 re 모듈을 사용한다. 이 중 sub 메소드는 정규식을 이용해 문자열을 치환하는 방법.
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        #정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]',  '', s)

        return s == s[::-1] #슬라이싱