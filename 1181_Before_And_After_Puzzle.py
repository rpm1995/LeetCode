class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:

        start = {}
        end = {}
        ans = set()

        for index, phrase in enumerate(phrases):

            phrase_split = phrase.split()
            first_word = phrase_split[0]
            last_word = phrase_split[-1]

            if first_word not in start:
                start[first_word] = set()
            start[first_word].add(index)

            if last_word not in end:
                end[last_word] = set()
            end[last_word].add(index)

        for last, last_indices in end.items():
            for last_index in last_indices:
                if last in start:
                    for first_index in start[last]:

                        if first_index != last_index:
                            if phrases[last_index].split()[:-1]:
                                ans.add(' '.join(phrases[last_index].split()[:-1]) + " " + phrases[first_index])
                            else:
                                ans.add(phrases[first_index])

        return sorted(ans)
