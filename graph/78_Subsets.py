
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        def dfs(path, start):
            for i in range(start, len(nums)):
                if path and i <= nums.index(path[-1]):
                    return
                                
                path.append(nums[i])
                result.append(path[:])
                dfs(path, i + 1)
                path.pop()
            
        dfs([], 0)
        return result
        

#answer in pdf
#이렇게 간결하게 짜고싶은데 흠
class Solution_pdf:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            #매번 결과 추가
            result.append(path)

            #경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        
        dfs(0, [])
        return result
    
nums = [4,1,0]
ans = Solution_pdf()
print(ans.subsets(nums))


