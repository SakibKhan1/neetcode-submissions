class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) 
        for word in strs:
            alphabet = [0] * 26 
            for char in word: 
                alphabet[ord('a') - ord(char)] += 1 
            hashmap[tuple(alphabet)].append(word) 

        return list(hashmap.values()) 