class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) <= len(str2):
            smaller = str1
            bigger = str2
        else:
            smaller = str2 
            bigger = str1 

        if str1 == str2:
            return str2 

        if not bigger.startswith(smaller):
            return "" 

        return self.gcdOfStrings(smaller, bigger[len(smaller):])