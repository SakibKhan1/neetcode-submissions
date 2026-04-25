class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        cars.sort(reverse = True)
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
            # else: current car joins the fleet ahead

        return len(stack)
