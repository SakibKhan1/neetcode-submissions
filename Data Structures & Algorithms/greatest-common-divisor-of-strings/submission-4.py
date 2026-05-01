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
        if str1 == str2:
            return str1
        left, right = 0, len(smaller) - 1 

        while left < right: 
            if str2[left: right + 1] * (len(bigger) // (right - left + 1)) == str1:
                return str2[left: right + 1]
            else:
                right -= 1 