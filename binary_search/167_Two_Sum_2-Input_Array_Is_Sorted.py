from typing import List
import bisect

#코드가 아주 그냥 누더기가 따로없네, Rustime도 121ms로 Bests 8.85% of users with Python3 에반데
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 방법 1
        # target보다 작은 리스트 원소들을 가지고 whilt left < right 해서 left 하나 씩 늘려가며
        # left + right 비교하고 인덱스 조절하면서 찾기

        # 방법 2
        # 위 방법을 binanry search로 해결하기

        index = bisect.bisect_right(numbers, target)
        # print(index)
        # numbers = numbers[:index] # 이거 target이 마이너스일 때 0 포함 안되는 거 떄문에 이렇게 했는데.. 좀 낭비가 심한듯
        
        # 또 target / 2 보다 큰 숫자들은 돌릴 필요가 없네
        for i in range(len(numbers)):
            if numbers[i] <= target / 2:
                pair = bisect.bisect_left(numbers, target - numbers[i])
                if len(numbers) > 0 and len(numbers) > pair and numbers[pair] == target - numbers[i]:
                    if i == pair: # numbers = [0,0,3,4], target = -1 이것 때문에 추가함
                        return [i + 1, pair + 2]
                    else:
                        return [i + 1, pair + 1]
                    
#sol1 two pointer
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1 # 리턴 값 + 1
            
#sol2 binary search
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v
            # 이진 검색으로 나머지 값 판별
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1
                

class Solution3:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k+1:], expected)
            if i < len(numbers[k + 1:]) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2
            

class Solution4:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k + 1:]
            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and numbers[i + k + 1] == expected:
                return k + 1, i + k + 2            

class Solution4:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1


# numbers = [2,7,11,15]
# target = 9
# numbers = [-1,0]
# target = -1
numbers = [0,0,3,4]
target = 0
print(Solution3().twoSum(numbers, target))