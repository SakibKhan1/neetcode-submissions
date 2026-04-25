class Solution:
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return (
                    self.isPali(s, left + 1, right)
                    or self.isPali(s, left, right - 1)
                )
            left += 1
            right -= 1

        return True
