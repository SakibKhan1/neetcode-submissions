from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mapping = defaultdict(list)
        trusts = set()

        for u, v in trust:
            mapping[v].append(u)
            trusts.add(u)

        counter = 0
        answer = -1

        for person in range(1, n + 1):
            # judge must trust nobody
            if person in trusts:
                continue

            # judge must be trusted by n - 1 people
            if len(mapping[person]) == n - 1:
                counter += 1
                answer = person

        if counter == 1:
            return answer

        return -1
