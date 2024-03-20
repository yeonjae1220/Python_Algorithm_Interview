
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(sum_list):
            if sum(sum_list) == target:
                result.append(sum_list[:])
            
            for e in candidates:
                if sum(sum_list) + e <= target:
                    if sum_list and sum_list[-1] <= e:
                        sum_list.append(e)
                        dfs(sum_list)
                        sum_list.pop()
                    elif not sum_list:
                        sum_list.append(e)
                        dfs(sum_list)
                        sum_list.pop()
        
        dfs([])
        return result

#pdf 답
#확실히 간결하고 좋다. 이렇게 코드 짜는 연습 하기
class Solution_pdf:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            #종료조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            
            #자신 부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result

candidates = [2,3,6,7]
target = 7
ans = Solution_pdf()
print(ans.combinationSum(candidates, target))