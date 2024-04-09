#처음부터 pdf보고 끝까지 함
import collections

class TrieNode:
    def __init__(self):
        self.word = False
        # self.child = {}
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # if char not in node.children:
            #     node.child[char] = TrieNode()
            node = node.children[char] # 만들고, 자식 노드로 내려가서 while문 반복
        node.word = True #끝에서 True 설정


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.word # if문에 안걸러졌으면 true return

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)