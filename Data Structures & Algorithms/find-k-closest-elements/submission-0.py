class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = -1
        res = float('inf')
        for i in range(len(arr)):
            if abs(x - arr[i]) < res:
                res = abs(x - arr[i]) 
                index = i
        if index == 0: 
            return arr[0: k]
        
        elif index == len(arr) - 1: 
            return arr[len(arr) - k: len(arr)]

        left = index - 1 
        right = index + 1 
        answer = [arr[index]] 
        i = 0 
        while i < k - 1:
            if abs(arr[index] - arr[left]) <= abs(arr[index] - arr[right]):
                answer.append(arr[left])
                left -= 1 
            else:
                answer.append(arr[right])
                right += 1 
            i += 1 

        return sorted(answer)