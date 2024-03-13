#make hash table about each chracters, and use two pointer to check lognest substring
#어우 이것저것 시행착오가 좀 있었음
import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        length = 0
        freqs = collections.defaultdict(int)
        front, rear = 0, 0

        for char in s:
            if not freqs[char]: #freqs[char] 이 0 일때 if문 실행
                freqs[char] += 1
                rear += 1
            
            else:
                freqs[char] += 1
                rear += 1
                while freqs[char] != 1 and rear >= front:
                    freqs[s[front]] -= 1
                    front += 1
                
                
            length = rear - front
            if longest_length < length:
                longest_length = length
            
        return longest_length
    

#solve in pdf
#위에 복잡하게 한거 대신 enumerate 썼으면 훨 편했음
class Solution_pdf:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
            
            used[char] = index

ans = Solution()
s = "tmmzuxt"
print(ans.lengthOfLongestSubstring(s))
                


