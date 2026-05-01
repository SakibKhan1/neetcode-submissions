from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for i in strs:
            value = 0 
            for char in i:
                value += ord(char) - ord("a")
            mapping[value].append(i)

        return list(mapping.values())