class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr:
            return 0

        currMax = 1
        globalMax = 1
        boolval = False  # True means last comparison was "<", False means ">"

        if len(arr) >= 2 and arr[0] < arr[1]:
            currMax = 2
            boolval = True
        elif len(arr) >= 2 and arr[0] > arr[1]:
            currMax = 2
            boolval = False

        for i in range(1, len(arr) - 1):
            if arr[i] == arr[i + 1]:
                currMax = 1
            elif boolval:
                if arr[i + 1] < arr[i]:
                    currMax += 1
                    boolval = False
                else:
                    currMax = 2
                    boolval = True
            else:
                if arr[i + 1] > arr[i]:
                    currMax += 1
                    boolval = True
                else:
                    currMax = 2
                    boolval = False

            globalMax = max(globalMax, currMax)

        return globalMax
