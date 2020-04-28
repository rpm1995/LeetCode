from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        n = len(deck)
        index = [i for i in range(n)]
        index = deque(index)
        deck.sort()
        ans = [-1 for _ in range(n)]
        current = 0

        while index:

            popped = index.popleft()
            ans[popped] = deck[current]

            if index:
                index.append(index.popleft())
                current += 1

        return ans
