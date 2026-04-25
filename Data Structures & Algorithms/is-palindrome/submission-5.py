class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1 
        while left < right:
            if self.AN(s[left]) == False:
                left += 1 
                continue
            if self.AN(s[right]) == False:
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1 
            right -= 1
        return True 
    def AN(self, char):
        if (ord("a") <= ord(char) <= ord("z") or
        ord("A") <= ord(char) <= ord("Z") or 
        ord('0') <= ord(char) <= ord('9')): 
            return True 
        return False 