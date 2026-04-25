class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list1 = list(word1[::-1])
        list2 = list(word2[::-1])

        res = [] 

        while list1 and list2:
            res.append(list1.pop())
            res.append(list2.pop())

        while list1:
            res.append(list1.pop())
        while list2:
            res.append(list2.pop())

        return "".join(res) 