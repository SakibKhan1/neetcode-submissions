from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        Tcounter = Counter(t) 
        left =0 
        window = {}
        have, need = 0, len(Tcounter)
        res = [-1,-1] 
        resLen = float("inf") 
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1 
            if c in Tcounter and Tcounter[c] == window[c]:
                have += 1 

            while have == need:
                if right - left + 1 < resLen:
                    res = [left, right]
                    resLen = right - left + 1 

                window[s[left]] -= 1 
                if s[left] in Tcounter and window[s[left]] < Tcounter[s[left]]:
                    have -= 1 
                left += 1 
        left, right = res #res will be [3,6] where 3 is left index and 6 is right index 

        return s[left:right+1] if resLen != float("inf") else "" 