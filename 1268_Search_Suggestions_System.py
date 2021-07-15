class Node():

    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.suggestions = []


class Trie():

    def __init__(self):

        self.root = Node()

    def insert(self, word):

        cur_node = self.root

        for char in word:

            if char not in cur_node.children:
                cur_node.children[char] = Node()
            cur_node = cur_node.children[char]

            cur_node.suggestions.append(word)
            cur_node.suggestions.sort()

            while len(cur_node.suggestions) > 3:
                cur_node.suggestions.pop()

        cur_node.end_of_word = True

    def search(self, word):

        res = []
        cur_node = self.root

        for char in word:

            if char not in cur_node.children:
                break
            cur_node = cur_node.children[char]
            res.append(cur_node.suggestions[:])

        l_remain = len(word) - len(res)

        for _ in range(l_remain):
            res.append([])

            # if char in cur_node.children:
            #     cur_node = cur_node.children[char]
            # res.append(cur_node.suggestions[:])

        return res


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        my_trie = Trie()
        ans = []

        for product in products:
            my_trie.insert(product)

        ans = my_trie.search(searchWord)

        return ans
