from typing import Optional
from typing import List
import converter_list2linkedlist
#self
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            interval = result.pop()
            if interval[1] >= intervals[i][0]:
                interval[1] = max(interval[1], intervals[i][1])
                result.append(interval)
            else:
                result.append(interval)
                result.append(intervals[i])
                
        return result

#pdf ans
#훨 깔끔하다. , 연산지 lambda 연산자
class Solution_1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
        return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))