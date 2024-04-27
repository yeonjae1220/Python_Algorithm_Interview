from typing import List
import collections
import re

"""
Runtime 40 ms Beats 51.98% of users with Python3 
Memory 16.56 MB Beats 73.68% of users with Python3
pdf 답안 보다 약간 느린듯?
굳이 defaultdict을 쓸 이유가 없었다. 괜히 더 복잡해진 느낌. 문자열 처리로 해결 보는게 이상적인듯
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        result = collections.defaultdict(int) # 초기값 이렇게 주나?
        paragraph = paragraph.lower()
        paragraph = re.sub('[!?\',;.]', ' ', paragraph)
        paragraph = paragraph.split()
        for word in paragraph:
            result[word] += 1

        result = sorted(result.items(), key= lambda x: x[1], reverse=True)
        
        for word, freq in result:
            if word not in banned:
                return word

        # result.items().sort(key= lambda x: x[1], reverse=True)
        
        
        return ""


"""
# leetcode sol
# 뭐 비슷함, 아래랑 다른 답안에서는 symbol = "!?',;." 해놓고 symbol 들 for 문 돌리면서 paragraph.replace(교체할 symbol, " ") 해서 바꿔주기도 함

"""
import re

class Solution_leetcode:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
		
		# convert to lower case and split string into words by spaces and punctuation
        a = re.split(r'\W+', paragraph.lower())
		
		# make new list consisitng of words not in banned list (remove banned words)
        b = [w for w in a if w not in banned]
		
		# return value that counted max times in the new list
        return max(b, key = b.count)


"""
pdf sol 대로 도전
"""
import re
import collections

class Solution_pdf:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word = re.sub('[^\w]', ' ', paragraph.lower()).split()
        word = collections.Counter(word)
        word = sorted(word.items(), key= lambda x: x[1], reverse=True)
        for w in word:
            if w[0] not in banned:
                return w[0]
        
        
        



paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(Solution_pdf().mostCommonWord(paragraph, banned))