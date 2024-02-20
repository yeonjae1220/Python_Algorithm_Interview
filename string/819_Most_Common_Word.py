#전부 소문자로 변경 후 Counter() 사용.
#나온 값이 banned와 같다면 그 다음 값을 리턴

#정규식에 대한 추가 공부 필요

#collections.Counter(a).most_common(n)   : a의 요소를 세어, 최빈값 n개를 반환합니다. (리스트에 담긴 튜플형태로)

#in, not in으로 문자열 포함 여부 확인 가능

#https://velog.io/@yoopark/r-prefix-in-regexp
#문자열 앞에 붙이는 r은 raw string의 의미를 가지며, 구체적인 의미는 \을 탈출 문자로 보지 않고, 그냥 아무 역할도 하지 않는 평범한 문자열로 간주하여 처리하겠다는 뜻이다.

#정규식이에서 \ 인데 / 로 써서 꽤 오래 해맴/

#35ms 16.51MB
import re
from typing import List
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split() 
                    if word not in banned]

        return Counter(words).most_common(1)[0][0]








# from collections import Counter
# from typing import List

# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         words = paragraph.lower()
#         ordered_words = list(Counter(words).keys)
#         if(ordered_words[0] != banned):
#             return ordered_words[0]
#         else:
#             return ordered_words[1]