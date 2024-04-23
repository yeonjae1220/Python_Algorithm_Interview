import re
"""
Runtime 45ms Beats 56.79% of users with Python3
Memory 18.01 MB Beats 20.96% of users with Python3
"""
# pdf sol is more simple.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        # its work but SyntaxWarning: invalid escape sequence '\W'
        # s = s.lower()
        # s = re.sub("\W", '', s)
        print(s)
        return s == s[::-1]
    

# leetcode sol, two lines
# Regular expressions are not necessary for this problem
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if s.isalnum()]
        return s == s[::-1]
    

# leetcode sol, O(1) space two-pointer
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i += 1
                    j += 1
                    continue
            
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        
        return True
        


s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))

