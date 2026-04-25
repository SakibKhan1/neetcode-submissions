class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        counter1 = 0
        counter2 = 0
        cand1 = None
        cand2 = None

        # First pass: find candidates
        for num in nums:
            if cand1 == num:
                counter1 += 1
            elif cand2 == num:
                counter2 += 1
            elif counter1 == 0:
                cand1 = num
                counter1 = 1
            elif counter2 == 0:
                cand2 = num
                counter2 = 1
            else:
                counter1 -= 1
                counter2 -= 1

        # Second pass: verify actual counts
        counter1 = 0
        counter2 = 0
        for num in nums:
            if num == cand1:
                counter1 += 1
            elif num == cand2:
                counter2 += 1

        target = len(nums) // 3  
        if counter1 > target:
            res.append(cand1)
        if counter2 > target:
            res.append(cand2)

        return res
