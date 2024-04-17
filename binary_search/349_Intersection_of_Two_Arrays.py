from typing import List, Set
import bisect

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))

        result = []
        for i in nums2:
            if i in nums1:
                result.append(i)

        return result


# sol1 brute force
# 위에게 55ms인데 얘는 85ms 나온다.
class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)
        
        return result
    
# sol2 binary search
class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        for n1 in nums1:
            # 이진 검색으로 일치 여부 판별
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)

        return result

"""
nums2 리스트가 비어있는 경우에는 i2에 대한 유효한 인덱스를 찾을 수 없습니다. 따라서 nums2 리스트가 비어있는 경우에는 조건문 안의 코드가 실행되면 안 됩니다.
bisect_left 함수는 해당 값이 삽입되어야 할 위치를 찾습니다. 따라서 i2는 리스트의 범위를 벗어날 수 있습니다. 이 경우에는 i2가 nums2 리스트의 길이를 초과하여 유효하지 않은 인덱스가 됩니다. 따라서 이 경우에도 조건문 안의 코드가 실행되면 안 됩니다.
마지막으로, n1이 nums2[i2]와 동일한지 확인하여 실제로 n1이 nums2 리스트에 존재하는지 확인합니다. 만약 n1이 nums2 리스트에 존재한다면, 조건문 안의 코드가 실행되어야 할 수 있습니다.
"""


# sol3 two pointer
class Solution3:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        # 양쪽 모두 정렬
        nums1.sort()
        nums2.sort()
        i = j = 0
        # 투 포인터 우측으로 이동하여 일치 여부 판별
        while j < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result


# nums1 = [1,2,2,1]
# nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution2().intersection(nums1, nums2))
