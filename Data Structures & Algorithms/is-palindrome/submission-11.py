class Solution:
    def isAlphaNum(self, s: str):
        if (ord('0') <= ord(s) <= ord('9') or
        ord('a') <= ord(s) <= ord('z') or 
        ord('A') <= ord(s) <= ord('Z')):
            return True 
        else:
            return False 
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1 

        while left < right:
            if not self.isAlphaNum(s[left]):
                left += 1 
                continue
            if not self.isAlphaNum(s[right]):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False 
            left += 1 
            right -= 1 
        return True 
