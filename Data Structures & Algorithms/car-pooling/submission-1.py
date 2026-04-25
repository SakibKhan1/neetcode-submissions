class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        localcounter = 0 
        for i in range(len(trips)):
            if localcounter > capacity:
                return False 
            if i < len(trips) - 1: 
                if trips[i + 1][1] < trips[i][2]:
                    localcounter += (trips[i][0] + trips[i + 1][0])

        return True 