from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.endofword = True

    def search(self, word: str) -> bool:
        n = len(word)
        q = deque([(self.root, 0)])  # (node, index in word)

        while q:
            node, i = q.popleft()

            if i == n:
                if node.endofword:
                    return True
                continue

            ch = word[i]
            if ch == '.':
                for child in node.children.values():
                    q.append((child, i + 1))
            else:
                if ch in node.children:
                    q.append((node.children[ch], i + 1))

        return False
