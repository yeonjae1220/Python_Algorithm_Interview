class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))