#각각의 문자열을 알파벳 순으로 정렬해서, 같은 것들 인덱스로 모으기. (딕셔너리로 2개의 리스트 합쳐봄)
#혹은 각각의 알파벳 종류의 수를 따로 저장?

#이런거 할 때 딕셔너리에 넣으면서 계산!

from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

anagrems = defaultdict(list)

for word in strs:
    anagrems[''.join(sorted(word))].append(word)

print(anagrems.values()) 

# sorted_strs = [''.join(sorted(word)) for word in strs]

# strs_dict = dict(zip(strs, sorted_strs))

# print(strs_dict)