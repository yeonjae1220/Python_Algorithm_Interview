#https://crackerjacks.tistory.com/14
# deepcopy에 대한 링크


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
ans = Solution()
print(ans.removeDuplicateLetters(s))
            
