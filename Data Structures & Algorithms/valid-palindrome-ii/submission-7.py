class Solution:
    def validPalindrome(self, s: str) -> bool:
        #return true if s can be a palindrome after deleting at most one character from it 
        #how to know which one to skip???
        #check if s[left + 1] == s[left] OR s[right - 1] == s[right] then we can use ONE skip

        use = 1 
        left, right = 0, len(s) - 1 
        if len(s) == 2:
            return True 
        while left <= right: 
            if s[left] == s[right]:
                left += 1 
                right -= 1

            elif (left + 1) == right:
                return True 

            else: 
                if use != 0:
                    if s[left + 1] == s[left]:
                        use -= 1 
                        right -= 1
                    elif s[right - 1] == s[right]:
                        use -= 1 
                        left += 1 
                    else:
                        return False 
                else:
                    return False 

        return True 