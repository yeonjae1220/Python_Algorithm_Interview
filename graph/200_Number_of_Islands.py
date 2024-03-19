#공부용으로 책보고 함, pdf 필기 참고
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or \
                  j < 0 or j >= len(grid[0]) or \
                      grid[i][j] != '1':
                return
            grid[i][j] = '2'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count
        


#check answer
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
ans = Solution()

print(ans.numIslands(grid))