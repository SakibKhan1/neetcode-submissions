class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Step 1: Combine positions and speeds manually into a list of pairs
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        # Step 2: Sort cars by position (descending)
        cars.sort(reverse=True)

        # Step 3: Use a stack to track fleets
        stack = []

        # Step 4: Iterate through each car
        for i in range(len(cars)):
            pos = cars[i][0]
            spd = cars[i][1]
            time = (target - pos) / spd

            # If this car takes longer than the fleet ahead, it becomes a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
            # else: this car joins the previous fleet (do nothing)

        return len(stack)
