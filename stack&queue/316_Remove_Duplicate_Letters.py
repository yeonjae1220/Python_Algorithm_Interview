#https://crackerjacks.tistory.com/14
# deepcopy에 대한 링크

from collections import Counter

class Solution_stack:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = Counter(s), []

        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)

        return ''.join(stack)

#re
class Solution_Divide_and_Conquer:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)): #set() 하면 중복 원소 제거 되나봄
            suffix = s[s.index(char):] # 반복문을 돌며 동일한 알파벳 확인

            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        
        return ''

class Solution_failed:
    def removeDuplicateLetters(self, s: str) -> str:
        list = ['A']
        #table = {}
        
        for w in s:
            if w in list:
                #below code, error occured that when I coding like this : temp_list = list[:].remove(w).append(w)
                temp_list = list[:]
                temp_list.remove(w)
                temp_list.append(w)
                if list >= temp_list:
                    list = temp_list
                
                #table.update(w = 'exist')
            #remove existing letter and input new letter in last of string
            
            else:
                list.append(w)


        return ''.join(list)



            
s = "bcabc"
ans = Solution_stack()
print(ans.removeDuplicateLetters(s))
            
