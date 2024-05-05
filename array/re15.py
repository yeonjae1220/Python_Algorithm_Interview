from typing import List
"""
leetcode sol 
"""
class Solution_leetcode:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res
        



"""
얘도 Time Limit Exceeded, 솔직히 3중 반복문이랑 똑같긴 함
"""




class Solution_failed2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            for i in range(len(nums)):
                temp = sorted([nums[i], target - nums[i], -target])
                if target - nums[i] in nums[i+1:]:
                    temp = sorted([nums[i], target - nums[i], -target])
                    if temp not in result: 
                        result.append(temp)
            
            return result
                    

        for i in range(len(nums) - 2):
            temp = twoSum(nums[i+1:], -nums[i])
            for i in range(len(temp)):
                if temp[i] not in result:
                    result.append(temp[i])
            
            
        return result
            



"""
2중 loop는 사용해야만 하는거 같은데.. 여기에 딕셔너리 붙여서 해보겠다.
어우 왤케 안풀리노 3중 루프 박아야겠다 -> 끔찍하네요  Time Limit Exceeded

from typing import List

class Solution_failed:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in result:
                        result.append(sorted([nums[i], nums[j], nums[k]]))
        
        return result
"""
        



#nums = [3,0,-2,-1,1,2]
nums = [-1,0,1,2,-1,-4]
print(Solution_leetcode().threeSum(nums))