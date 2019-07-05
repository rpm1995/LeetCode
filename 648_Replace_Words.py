class Node():
    def __init__(self):
        self.children = {}
        self.endofword = False
        self.string = ""


class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        pointer = self.root

        for char in word:
            if char not in pointer.children:
                pointer.children[char] = Node()
            pointer = pointer.children[char]

        pointer.endofword = True
        pointer.string = word

    def search(self, word):
        pointer = self.root

        for char in word:
            if char not in pointer.children:
                # print("here")
                return ""
            pointer = pointer.children[char]

            if pointer.endofword is True:
                return pointer.string

        return ""


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:

        prefixtree = Trie()
        ans = ""

        for word in dict:
            prefixtree.insert(word)

        for word in sentence.split():
            root = prefixtree.search(word)

            if root == "":
                ans += word
            else:
                ans += root
            ans += " "

        return ans[:-1]
