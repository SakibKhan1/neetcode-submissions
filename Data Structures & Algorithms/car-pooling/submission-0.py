class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        localcounter = 0 
        time = 1
        for i in range(len(trips)):
            if i > 0 and trips[i - 1][2] == time:
                localcounter = 0 
            localcounter += trips[i][0]
            if localcounter > capacity:
                return False
            time += 1 

        return True 