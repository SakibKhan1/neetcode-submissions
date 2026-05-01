class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        longest = 0 
        sett = set() 

        for right in range(len(s) - 1): 
            while s[right] in sett: 
                sett.remove(s[left])
                left += 1 
            sett.add(s[right]) 
            window_size = right - left + 1 
            longest = max(window_size, longest) 

        return longest 