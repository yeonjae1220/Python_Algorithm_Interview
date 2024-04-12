from typing import Optional
from typing import List
import converter_list2linkedlist

#pdf 해답
#아이디어는 같고, 구현 능력 부족
class Solution:
    # @staticmethod 데코레이터를 사용하여 정의된 메서드는 클래스의 인스턴스를 생성하지 않고도 호출될 수 있습니다.
    # 이거 안 붙이니 아래 self.to_swap 쓸 때 argument 3개 들어온다 하네
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)
    
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))

class Solution_failed:
    def largestNumber(self, nums: List[int]) -> str:
        str_list = []
        result = ""
        for i in range(len(nums)):
            str_list.append(str(nums[i]))
        
        str_list.sort(reverse=True)

        # 정렬된 배열 i와 i+1 사이 문자열 합으로 비교하며 스왑했는데 실패
        #for i in range(len(str_list) - 1):
            # if str_list[i]+str_list[i+1] < str_list[i+1] + str_list[i]:
            #     str_list[i], str_list[i+1] = str_list[i+1], str_list[i]    
            # result += str_list[i]

        # 위 방법을 인덱스를 뒤집어서 시도했지만 실패
        # for i in range(len(str_list) - 1, 0, -1):
        #     if str_list[i]+str_list[i-1] > str_list[i-1] + str_list[i]:
        #         str_list[i], str_list[i-1] = str_list[i-1], str_list[i]
        #         i += 1

        ### 통상적으로 같은 수가 여러번 나오는 상황에서 wrong answer가 자주발생

        for i in range(len(str_list)):
            result += str_list[i]

        return str(int(result))


# nums = [3,30,34,5,9] 43243 243    43243 432
# nums = [0,0]
# nums = [432,43243]

# nums = [74,21,33,51,77,51,90,60,5,56]
# 90 77 74 60 56 51 5 51 33 21
# 90 77 74 60 56 5 51 51 33 21

nums = [5,54,52,67,68,5,52,17,93,53]

# 93 68 67 54 53 52 52 17 5 5
# 93 68 67 5 54 53 52 52 5 17
# 93 68 67 5 5 54 53 52 52 17

print(Solution().largestNumber(nums))