from typing import List
import collections

#엄청 긴 input에 대해 time limit exceed
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        string = ""
        for i in range(len(words)):
            for j in range(len(words) - 1, -1, -1):
                if not i == j:
                    string = words[i] + words[j]
                    if string == string[::-1]:
                        result.append([i, j])
        return result
                    

#pdf bruteforce (얘도 시간 초과로 풀리지 않을 것임), 위에 내가 해놓은것 보다 그래도 깔끔
class Solution_1:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palidrome(word):
            return word == word[::-1]
        
        output = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if is_palidrome(word1 + word2):
                    output.append([i, j])
        return output
    


#trie로 푸는 법
class TrieNode:
    def __init__(self):
        self.childern = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrom_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> None:
        return word[::] == word[::-1]
    
    #단어 삽입
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrom_word_ids.append(index)
            node = node.childern[char]
            # node.val = char
        node.word_id = index

    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            #판별로직
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.childern:
                return result
            node = node.childern[word[0]]
            word = word[1:]

        # 판별 로직
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 판별 로직
        for palindrome_word_id in node.palindrom_word_ids:
            result.append([index, palindrome_word_id])

        return result

class Solution_2:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        result = []
        for i, word in enumerate(words):
            result.extend(trie.search(i, word))

        return result
        




# words = ["abcd","dcba","lls","s","sssll"]
# words = ["bat","tab","cat"]
words = ["a",""]
print(Solution_2().palindromePairs(words))

