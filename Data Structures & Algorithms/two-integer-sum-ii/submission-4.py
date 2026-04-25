class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {} 
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in hashmap:
                if hashmap[difference] < i:
                    return [hashmap[difference] + 1, i + 1]
                else:
                    return [i + 1, hashmap[difference] + 1]
            hashmap[numbers[i]] = i 