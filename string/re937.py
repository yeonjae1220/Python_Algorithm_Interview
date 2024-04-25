from typing import List
"""
Runtime 41 ms Beats 58.32% of users with Python3 
Memory 16.74 MB Beats 23.09% of users with Python3
pdf랑 거의 동일
"""
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        result_alpa = []
        result_num = []
        for log in logs:
            content = log.split(maxsplit=1)[1]
            if content[0].isalpha():
                result_alpa.append(log)
            else:
                result_num.append(log)

        result_alpa.sort(key=lambda x: (x.split(maxsplit=1)[1], x.split(maxsplit=1)[0])) # If their contents are the same, then sort them lexicographically by their identifiers.


        return result_alpa + result_num

# 동일한 방법, 함수를 나누어서 조금 더 간결
class Solution_leetcode:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs,key = self.sort)
    def sort(self,logs):
            a,b = logs.split(' ', 1)
            if b[0].isalpha():
                return (0,b,a)
            else:
                return (1,None,None)

# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
print(Solution().reorderLogFiles(logs))


"""
막 한줄로 코드 뚝딱 만들고 싶은데 구현 능력이 부족하네,, 어케하더라

x.split(maxsplit=1) 로 하는 것이 아닌 x.split()[1:] 로 슬라이싱 처리하는게 더 좋아보이네

람다는 간단한 함수를 쉽게 선언하는 방법이다.
보통 람다 표현식 보다는 더욱 간결하고 가독성이 높은 라스트 컴프리헨션(List Comprehension) 사용 추천
람다로 푸는게 편할 경우 이렇게 일부 사용

"""
