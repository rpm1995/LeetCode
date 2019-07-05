class Node:
    def __init__(self):
        self.children = {}
        self.wordend = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        pointer = self.root

        for char in word:
            if char not in pointer.children:
                pointer.children[char] = Node()
            pointer = pointer.children[char]

        pointer.wordend = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        stack = [(word, self.root)]

        while stack:

            curword, curnode = stack.pop()

            if not curword:
                if curnode.wordend is True:
                    return True
                # else:
                #     return False

            elif curword[0] == ".":
                for kid in curnode.children.values():
                    stack.append((curword[1:], kid))

            else:
                if curword[0] in curnode.children:
                    curnode = curnode.children[curword[0]]
                    stack.append((curword[1:], curnode))

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
