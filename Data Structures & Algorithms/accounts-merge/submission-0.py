from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        email_to_name = {}

        # 1. Build graph
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email] = name

        visited = set()
        res = []

        # 2. DFS to find connected components
        def dfs(email, component):
            visited.add(email)
            component.append(email)

            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, component)

        # 3. Traverse all emails
        for email in graph:
            if email not in visited:
                component = []
                dfs(email, component)
                component.sort()
                res.append([email_to_name[email]] + component)

        return res
