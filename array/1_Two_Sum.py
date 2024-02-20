nums = [2,7,11,15] 
target = 9

#brute force
# for i in range(len(nums) - 1):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print([i, j])


#search with 'in'
#얘도 전체 시간 복잡도는 동일하지만 brute force보다는 훨씬 가볍고, 더 빠르다.
#enumerate() 함수는 index와 elements를 동시에 접근한다.
#슬라이싱을 이렇게도 사용하네
#.index()
# for i, n in enumerate(nums):
#     complement = target - n

#     if complement in nums[i + 1:]:
#         print([i, nums[i+1:].index(complement) + (i + 1)]) #여기서 (i + 1)은 complement 찾는 리스트가 i 뒤에서 시작하기 때문


#첫 번째 수를 뺀 결과 키 조회 (175p)
#딕셔너리를 조회하면 평균적으로 O(1)로 가능하다. #딕셔너리 만드는 시간 복잡도는?
#딕셔너리를 in 으로 찾을 때 key값만 보는듯. value는 안보는듯?
# nums_map = {}
# for i, num in enumerate(nums):
#     nums_map[num] = i

# for i, num in enumerate(nums):
#     if target - num in nums_map and i != nums_map[target - num]:
#         print(i, nums_map[target - num])


#조회 구조 개선
#위에 for문 2개 있는거 합친거임
# nums_map = {}
# for i, num in enumerate(nums):
#     if target - num in nums_map:
#         print([nums_map[target - num], i])
#     nums_map[num] = i


#two pointer 이용

#다른 언어 이용