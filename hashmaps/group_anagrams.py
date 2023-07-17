from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_word = {}

        sorted_word = defaultdict(list)

        final = []

        for i in strs:
            key = tuple(sorted(i))
            sorted_word[key].append(i)

        for values in sorted_word.values():
            final.append(values)

        return final
