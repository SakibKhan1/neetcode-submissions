class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        answer = 0 
        for i in operations:
            if i == "+":
                ans = res[-1] + res[-2]
                res.append(ans)
            elif i == "D":
                ans = res[-1] * 2 
                res.append(ans) 

            elif i == "C":
                res.pop()
            else:
                res.append(int(i)) 

        return sum(res) 