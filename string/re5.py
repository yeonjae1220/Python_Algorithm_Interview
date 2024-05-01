# re
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <=2 or s[:] == s[::-1]:
            return s
        
        
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1:right-1]
            #이렇게 하니 "cbbd" 에서 cbb 나온다.
            # while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
            #     left -= 1
            #     right += 1
            # return s[left:right+1]
        
        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i,i+1), expand(i,i+2), key=len)
        
        return result


# 함수로 안 빼고 그냥 풀어봄
class Solution_long:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <=2 or s[:] == s[::-1]:
            return s
        
        result = ''
        
        for i in range(len(s)-1):
            left = i
            right = i+1
            while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            result = max(result, s[left:right+1], key=len)
        
        for i in range(len(s)-1):
            left = i
            right = i+2
            while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            result = max(result, s[left:right+1], key=len)

        return result
        
        

            
                
        
s = "cbbd"#"babad"

print(Solution().longestPalindrome(s))