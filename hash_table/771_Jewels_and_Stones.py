#solve with counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for char in stones:
            if char in jewels:
                cnt += 1
        return cnt

import collections    
#solve with counter in pdf
class Solution_counter:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones) # calculate stones frequence
        cnt = 0
        for char in jewels:
            cnt += freqs[char]
        return cnt


#solve with hash table in pdf
class Solution_hash:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        cnt = 0
        for char in stones:
            #처음에 freqs에 뭐가 없어서 이렇게 if else로 구분함
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        
        for char in jewels:
            cnt += freqs[char]
        
        return cnt
    

#solve with hash table & defaultdict()
class Solution_defaultdict:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int) #Type specification
        cnt = 0

        for char in stones:
            freqs[char] += 1
        
        for char in jewels:
            cnt += freqs[char]
        
        return cnt
    
#solve with pythonic way
class Solution_pythonic:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)

ans = Solution_defaultdict()
jewels = "aA" 
stones = "aAAbbbb"
print(ans.numJewelsInStones(jewels, stones))
