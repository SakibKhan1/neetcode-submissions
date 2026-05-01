class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping = {}

        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in mapping:
                return [[mapping[difference], i]]
            mapping[difference] = i 