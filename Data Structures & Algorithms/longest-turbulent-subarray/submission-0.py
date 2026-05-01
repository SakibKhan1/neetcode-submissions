class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        currMax = 1
        globalMax = 0 
        currElement = arr[0]
        boolval = False 

        if len(arr) >= 2 and arr[0] < arr[1]:
            currMax += 1 
            boolval = True 
        elif len(arr) >= 2 and arr[0] > arr[1]:
            currMax +=1 
            boolval = False
        else:
            boolval = False 

        for i in range(1, len(arr) - 1):
            if arr[i] == arr[i + 1]:
                currMax = 1
                continue
            elif boolval == True: 
                if arr[i + 1] < arr[i]:
                    currMax += 1 
                    boolval = False 
            else:
                if arr[i + 1] > arr[i]:
                    currMax += 1 
                    boolval = True 

            globalMax = max(globalMax, currMax)
    
        return globalMax