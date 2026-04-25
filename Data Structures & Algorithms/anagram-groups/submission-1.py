from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a dictionary, where the key is a lettersarray and the value are the words
        #.. that match that lettersarray (.append() ) 
        result = defaultdict(list) 

        for word in strs:
            lettersarray = [0] * 26 
            for letter in word:
                lettersarray[ord(letter) - ord('a')] += 1
            result[tuple(lettersarray)].append(word) 

        return list(result.values()) 