from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        #         # Depth-First Search Approach
        # def helper(cur_word, end_word, visited, length):

        #             if cur_word == end_word:
        #                 self.ans = min(self.ans, length)
        #                 return

        #             else:
        #                 visited.add(cur_word)
        #                 original = cur_word

        #                 for index, char in enumerate(cur_word):
        #                     for new_char in "abcdefghijklmnopqrstuvwxyz":
        #                         cur_word = cur_word[:index] + new_char + cur_word[index+1: ]

        #                         if cur_word in words and cur_word not in visited:
        #                             # print(cur_word)
        #                             helper(cur_word, end_word, visited, length+1)
        #                     cur_word = original

        #                 visited.remove(original)

        #             return

        #         self.ans = float('inf')
        #         words = set(wordList)
        #         helper(beginWord, endWord, set(), 1)
        #         return self.ans if self.ans != float('inf') else 0

        # Breadth First Search Approach
        words = set(wordList)
        queue = deque([])
        queue.append([beginWord, 1])
        visited = set()
        visited.add(beginWord)

        if beginWord == endWord:
            return 1

        while queue:
            cur_word, length = queue.popleft()
            visited.add(cur_word)

            if cur_word == endWord:
                return length

            for index, char in enumerate(cur_word):
                for new_char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = cur_word[:index] + new_char + cur_word[index + 1:]

                    if new_word in words and new_word not in visited:
                        queue.append([new_word, length + 1])
                        visited.add(new_word)  # IMPORTANT because this is the earliest we will ever see this word

        return 0
