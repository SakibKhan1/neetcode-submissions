class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        worddict = defaultdict(list) 
        
        for word in strs:
            lettercount = [0] * 26 
            for char in word: 
                lettercount[ord(char) - ord('a')] += 1 
            worddict[tuple(lettercount)].append(word) 


        return list(worddict.values()) 