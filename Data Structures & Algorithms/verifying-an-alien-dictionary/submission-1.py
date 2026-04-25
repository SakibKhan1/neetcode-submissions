class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {v: i for i,v in enumerate(order)}
        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            for j in range(len(min(w1,w2,key=len))):
                diff = False 
                if w1[j] != w2[j]:
                    diff = True 
                    if mapping[w1[j]] > mapping[w2[j]]:
                        return False 
                    break 
            if diff == False and len(w1) > len(w2):
                return False 

        return True 
            