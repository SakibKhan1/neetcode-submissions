class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for word in strs:
            asciichart = [0] * 26 
            for char in word:
                asciichart[ord('a') - ord(char)] += 1 
            mapping[tuple(asciichart)].append(word)

        return list(mapping.values())