class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smaller = min(str1,str2, key = len) 
        bigger = max(str1, str2) 
        if smaller not in bigger:
            return "" 
        
        left, right = 0, len(smaller) - 1 

        while left < right: 
            if str2[left: right + 1] * (len(bigger) // (right - left + 1)) == str1:
                return str2[left: right + 1]
            else:
                right -= 1 