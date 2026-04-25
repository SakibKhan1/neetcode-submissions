class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smaller, bigger = None, None 
        if len(str1) <= len(str2):
            smaller = str1
            bigger = str2 
        else:
            smaller = str2 
            bigger = str1 

        if str1 + str2 != str2 + str1:
            return "" 

        left, right = 0, len(smaller) - 1 

        while left <= right: 
            candidate = smaller[left:right + 1]
            length = right - left + 1

            if len(bigger) % length == 0 and len(smaller) % length == 0:
                if candidate * (len(bigger) // length) == bigger and \
                   candidate * (len(smaller) // length) == smaller:
                    return candidate

            right -= 1

        return ""