class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right = len(s) - 1
        halflen = len(s) // 2 
        for i in range(halflen):
            s[i], s[right] = s[right], s[i]
            right -= 1 
