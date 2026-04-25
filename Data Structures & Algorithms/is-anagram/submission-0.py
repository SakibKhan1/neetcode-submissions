class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = sorted(s), sorted(t)
        if(a == b):
            return True
        else:
            return False