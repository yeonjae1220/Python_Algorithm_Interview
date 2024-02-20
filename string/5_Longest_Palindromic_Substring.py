#문자열 index 0 하고 1부터 보면서 해당 index-1, index+1이 같은지 확인. 


#def expand 에서 index 주의!! 오류 많이 남

#range(1, 10)은 1~9


s = "ac"


def expand(left: int, right: int) -> str:
    while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
        left -= 1
        right += 1
    return s[left + 1: right - 1]


if len(s) < 2 or s == s[::-1]:
    print(s)

result = ''

for i in range(len(s) - 1):
    result = max(result, expand(i, i+1), expand(i, i+2), key=len)

print(result)
