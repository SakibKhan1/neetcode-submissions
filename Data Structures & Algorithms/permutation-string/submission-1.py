class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {} #freq_dict 
        hashmap2 = {} #dictionary for s2's windows of freq 
        s1length = len(s1) 
        
        if len(s2) < s1length:
            return False 
            
        for i in s1:
            hashmap[i] = hashmap.get(i, 0) + 1 
        
        for i in range(0, s1length):
            hashmap2[s2[i]] = hashmap2.get(s2[i], 0) + 1 
            
        if hashmap2 == hashmap:
            return True 
            
        for i in range(s1length, len(s2)):
            hashmap2[s2[i]] = hashmap2.get(s2[i], 0) + 1 
            hashmap2[s2[i - s1length]] -= 1
            if hashmap2[s2[i - s1length]] == 0:
                del hashmap2[s2[i - s1length]]
            if hashmap2 == hashmap:
                return True 
        return False 