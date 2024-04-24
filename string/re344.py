from typing import List

"""
Runtime 169 ms Beats 61.25% of users with Python3 
Memory 20.74 MB Beats 93.55% of users with Python3
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

"""
Runtime 164 ms Beats 82.97% of users with Python3
Memory 20.97 MB Beats 46.02% of users with Python3
"""
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        """
        print(id(s))
        s = s.reverse()
        print(id(s))
        """
        
        """
        print(id(s))
        s = s[::-1]
        print(id(s))
        # https://leetcode.com/problems/reverse-string/solutions/670137/python-3-actually-easiest-solution/

        """
        
        


s = ["h","e","l","l","o"]
print(id(s))
Solution().reverseString(s)
print(s)