from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if(log.split()[1].isalpha()):
                letters.append(log)
            else:
                digits.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
    
    #sort는 key를 이용해서 여러가지 기준으로 정렬을 실행할 수 있다.
    #lambda로 간단한 함수를 쉽게 선언.

    #36ms 16.89MB