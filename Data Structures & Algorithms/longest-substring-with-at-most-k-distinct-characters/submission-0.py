class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0 
        right = 0 
        res = 0 
        mapping = {} 
        while right < len(s):
            mapping[s[right]] = mapping.get(s[right], 0) + 1 
            if len(mapping) > k:
                mapping[s[left]] -= 1
                if mapping[s[left]] == 0:
                    del mapping[s[left]]
                left += 1
            res = max(res, right - left + 1)
            right += 1 
        return res 