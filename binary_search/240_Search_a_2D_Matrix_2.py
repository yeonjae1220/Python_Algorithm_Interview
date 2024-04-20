from typing import List

class Solution_failed:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 대각선으로 내려가며 matrix 쪼개가면서 할려다가 패스
        # temp = max(len(matrix), len(matrix[0]))

        # 제일 끝값이랑 처음 값 범위 밖이면 없는거고, x축 y축 binary search해서 얘보다 작은 범위 자르고, 나머지 브루트 포스 해봄
        if target < matrix[0][0] and matrix[-1][-1] < target:
            return False
        
        x, y = 0, 0
        for i in range(len(matrix[0])):
            if matrix[0][i] >= target:
                x = i
                break
        
        for j in range(len(matrix)):
            if matrix[j][0] >= target:
                y = j
                break

        #0, 0 일 때 못걸러 낸다 

        for i in range(1, x + 1):
            for j in range(1, y + 1):
                if matrix[i - 1][j - 1] == target:
                    return True
        
        return False
    

# 첫 항의 맨 뒤에서 탐색
# 이러면 되는구나
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 예외 처리
        if not matrix:
            return False
        
        # 첫 항의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타깃이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            # 타깃이 크면 아래로 이동
            elif target > matrix[row][col]:
                row >= 1
            return False
        
# Pythonic way
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)
                

# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 5
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
# matrix = [[-5]]
# target = -5


print(Solution2().searchMatrix(matrix, target))