class Node:
    def __init__(self):
        self.children = {}
        self.storedsentence = ""
        self.end = False
        self.hot = 0


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Node()
        self.cursentence = ""

        for sentence, time in zip(sentences, times):
            self.adddata(sentence, time)

    def adddata(self, sentence, time):
        pointer = self.root

        for char in sentence:
            if char not in pointer.children:
                pointer.children[char] = Node()
            pointer = pointer.children[char]

        pointer.storedsentence = sentence
        pointer.end = True
        pointer.hot -= time

    def search(self, sentence):
        pointer = self.root
        result = []
        stack = []

        for char in sentence:
            if char not in pointer.children:
                return []
            pointer = pointer.children[char]

        stack.append(pointer)

        while stack:
            curnode = stack.pop(0)

            if curnode.end is True:
                result.append((curnode.hot, curnode.storedsentence))

            stack.extend(curnode.children.values())

        return result

    def input(self, c: str) -> List[str]:

        result = []

        if c != "#":
            self.cursentence += c
            result = self.search(self.cursentence)
        else:
            self.adddata(self.cursentence, 1)
            self.cursentence = ""

        # print(sorted(result, key=lambda x: (x[0], x[1]), reverse=True))
        # result.sort(key=lambda x: (x[0], x[1]), reverse=True)
        # print(result)
        # return [item[1] for item in sorted(result, key=lambda x: (x[0], x[1]), reverse=True)[:3]]
        return [item[1] for item in sorted(result)[:3]]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
