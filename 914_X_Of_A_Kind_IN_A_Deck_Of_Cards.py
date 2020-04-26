class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        def gcd(a, b):

            while b:
                a, b = b, a % b

            return a

        card_counts = {}
        counts = []

        for card in deck:

            if card not in card_counts:
                card_counts[card] = 0
            card_counts[card] += 1

        for count in card_counts.values():
            counts.append(count)

        return reduce(gcd, counts) > 1
