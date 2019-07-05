class Trie:
    class node:
        def __init__(self):
            self.children = {}
            self.endofword = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pointer = self.root

        for char in word:
            if char not in pointer.children:
                pointer.children[char] = self.node()
            pointer = pointer.children[char]

        pointer.endofword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pointer = self.root

        for char in word:
            if char not in pointer.children:
                return False
            pointer = pointer.children[char]

        return pointer.endofword

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pointer = self.root

        for char in prefix:
            if char not in pointer.children:
                return False
            pointer = pointer.children[char]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)