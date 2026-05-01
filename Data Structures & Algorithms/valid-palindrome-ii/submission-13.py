class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1 
        boolval = False
        while left <= right: 
            if s[left] == s[right]:
                left += 1 
                right -= 1 
            elif s[left] != s[right]:
                if s[left + 1] == s[right]:
                    left += 1 
                    boolval = True 
                elif s[right - 1] == s[left]:
                    right -= 1 
                    boolval = True 
                else:
                    return False 
        return True 