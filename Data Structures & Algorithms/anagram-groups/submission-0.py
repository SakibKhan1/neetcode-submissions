class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            counter = [0] * 26 
            for char in word:
                counter[ord(char) - ord('a')] += 1 
            if tuple(counter) not in hashmap:
                hashmap[tuple(counter)] = [] 
            hashmap[tuple(counter)].append(word) 
        return list(hashmap.values())