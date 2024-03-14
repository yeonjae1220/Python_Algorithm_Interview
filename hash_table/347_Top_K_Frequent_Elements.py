#1t failed
from typing import List
import collections, heapq
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         sorted_nums = sorted(nums)
#         freqs = collections.Counter(sorted_nums)
#         result = []
#         for i in freqs: #오답! 딕셔너리 이렇게 해서 돌릴 때 그냥 입력받은 리스트 순서대로 출력이 나오는듯
#             if k == 0:
#                 break
#             result.append(i)
#             k -= 1
#         return result

class Solution_counter:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = collections.Counter(nums)
        freqs_heap = []
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f)) #빈도수가 큰 수부터 쓰기 위해서

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk
        
#zip 과 *에 대해 pdf에 있다. 각각에 대해 여러 쓰임이 있다.
class Solution_pythonic_way:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
nums = [4,1,-1,2,-1,2,3]
k = 1

ans = Solution()
print(ans.topKFrequent(nums, k))

# freqs = collections.Counter(nums)
# print(freqs)
# for i in freqs:
#     print(i)
    
    
    