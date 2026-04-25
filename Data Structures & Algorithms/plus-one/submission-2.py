class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [] 
        for i in digits:
            res.append(str(i))

        number = "".join(res)

        newnumber = list(str(int(number) + 1))
        res2 = []
        for i in newnumber:
            res2.append(int(i))

        return res2