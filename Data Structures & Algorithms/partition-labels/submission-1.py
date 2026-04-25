class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {} 
        for i in range(len(s)): 
            hashmap[s[i]] = i 
        res = [] 
        left,right = 0,0 
        stop = float('-inf')
        while right < len(s):
            stop = max(stop, hashmap[s[right]])
            if right == stop: 
                res.append(right - left + 1)
                left = right + 1 
            right += 1 

        return res 
