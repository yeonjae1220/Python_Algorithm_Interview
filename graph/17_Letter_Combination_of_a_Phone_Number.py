
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def dfs(word, index):
            if len(word) == length:
                result.append(word)
                return
            
            for i in range(index, length): #이렇게 하는걸 생각을 못했었음
                for j in dic[digits[index]]:
                    dfs(word + j, i + 1)
                
        if not digits:
            return []

        dic = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6": "mno",
               "7" : "pqrs", "8" : "tuv", "9": "wxyz"}
        result = []
        length = len(digits)
        dfs("", 0)

        return result


        
digits = "23"
ans = Solution()
print(ans.letterCombinations(digits))