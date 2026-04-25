from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for i in strs:
            word = [0] * 26 
            for char in i:
                word[ord("a") - ord(char)] += 1 
            mapping[tuple(word)].append(i)
        return list(mapping.values())