class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the array to enable two-pointer approach

        for i in range(len(nums)):
            # Optimization: since array is sorted, no need to continue if current number is > 0
            if nums[i] > 0:
                break

            # Skip duplicate values for the first number of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Set up two pointers
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1  # Need a smaller sum, move right pointer left
                elif threeSum < 0:
                    l += 1  # Need a larger sum, move left pointer right
                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicates on the left
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicates on the right
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res