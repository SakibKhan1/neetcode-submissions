class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapping = {0: 1}
        currsum = 0
        res = 0

        for num in nums:
            currsum += num
            calc = currsum - k

            if calc in mapping:
                res += mapping[calc]

            mapping[currsum] = mapping.get(currsum, 0) + 1

        return res
