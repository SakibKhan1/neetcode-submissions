class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []   # changed from string to list

        smallest = min(len(word1), len(word2))
        pointer1 = 0
        pointer2 = 0

        while pointer1 < smallest and pointer2 < smallest:
            res.append(word1[pointer1])
            pointer1 += 1

            res.append(word2[pointer2])
            pointer2 += 1

        if smallest == len(word1):
            res.append(word2[pointer2: len(word2)])
        elif smallest == len(word2):
            res.append(word1[pointer1: len(word1)])

        return "".join(res)
