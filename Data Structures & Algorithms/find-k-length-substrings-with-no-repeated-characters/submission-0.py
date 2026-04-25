class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        left = 0 
        right = 0 
        visited = set()
        res = 0 
        while right < len(s):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1 
            visited.add(s[right])
            if (right - left + 1) == k:
                res += 1 
                visited.remove(s[left])
                left += 1
            elif (right - left + 1) > k:
                visited.remove(s[left])
                left += 1
            right += 1 
        return res 