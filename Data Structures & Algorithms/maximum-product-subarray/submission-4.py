class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minDP = nums[:]
        maxDP = nums[:]
        result = nums[0]
        for i in range(1, len(nums)):
            minDP[i] = min(nums[i], nums[i] * minDP[i - 1], nums[i] * maxDP[i - 1])
            maxDP[i] = max(nums[i], nums[i] * maxDP[i - 1], nums[i] * minDP[i - 1])

            result = max(result, maxDP[i])

        return result 