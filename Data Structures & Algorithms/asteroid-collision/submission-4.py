class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            while stack and asteroids[i] < 0 and stack[-1] > 0:
                if abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(stack[-1]) > abs(asteroids[i]):
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroids[i])

        return stack
