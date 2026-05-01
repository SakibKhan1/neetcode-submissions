class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[position[i], speed[i]] for i in range(len(position))]
        pairs.sort(reverse = True) 
        # ex: [[7,1], [5,2], [1,3], [position, speed] ..]

        fleets = 1 
        prevtime = ((target - pairs[0][0]) / pairs[0][1])

        for i in range(1, len(pairs)):
            currtime = ((target - pairs[i][0]) / pairs[i][1])
            if currtime > prevtime: 
                fleets += 1 
                currtime = prevtime 
        return fleets 