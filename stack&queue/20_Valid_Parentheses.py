class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char not in table:
                stack.append(char)

            elif not stack or stack.pop() != table[char]: #elif 안하고 if 해서 에러 났음
                return False
        
        return len(stack) == 0
        #return True 해서 input이 "[" 일때 wrong answer 뜸
        

s = "()"
ans = Solution()
print(ans.isValid(s))

