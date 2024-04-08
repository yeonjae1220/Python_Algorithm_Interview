from typing import Optional
from typing import List
import collections
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
        # nums.sort()
        # return nums[-k]
    
# heapq 모듈 이용
# heapq는 최소힙만 저장, 음수로 저장해서 가장 낮은 수부터 추출해 부호 변환하면 최대 힙처럼 동작.
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)

# heapq 모듈의 heapify 이용
# heapify는 주어진 자료구조가 힙 특성을 만족하도록 바꿔주는 연산임
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
    
# heapq 모듈의 nlargest 이용
# heap이 아니더라도 내부적으로 heapify() 함수도 호출해 처리해 주어 편리
# nsmallest()를 사용하면 동일한 방식으로 n번째 작은값도 추출 가능

class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:    
        return heapq.nlargest(k, nums)[-1]
    

nums = [3,2,1,5,6,4] 
k = 2
print(Solution().findKthLargest(nums, k))