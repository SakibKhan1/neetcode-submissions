class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxDP = nums[:]      # max product ending at i
        minDP = nums[:]      # min product ending at i

        result = nums[0]

        for i in range(1, len(nums)):
            mx = maxDP[i-1]
            mn = minDP[i-1]

            maxDP[i] = max(nums[i], nums[i] * mx)
            minDP[i] = min(nums[i], nums[i] * mn)

            result = max(result, maxDP[i])

        return result
