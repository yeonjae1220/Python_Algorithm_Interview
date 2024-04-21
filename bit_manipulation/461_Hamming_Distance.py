class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        and_bit = bin(x ^ y)
        result = 0
        print(and_bit)
        print(type(and_bit))
        for i in and_bit:
            if i == '1':
                result += 1
        return result
    
# pdf sol, 너무 간단
class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
    
x = 1
y = 4
print(Solution1().hammingDistance(x, y))


