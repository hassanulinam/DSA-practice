# https://leetcode.com/problems/car-fleet
def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    stack = []
    n = len(position)
    fleets = 0
    for i in range(n - 1, -1, -1):
        current_mile = position[i] + speed[i]
        if current_mile <= target and current_mile != stack[-1]:
            stack.append(current_mile)
            fleets += 1

    return fleets


inputs = [
    (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]),
    (10, [3], [3]),
    (100, [0, 2, 4], [4, 2, 1]),
]
for target, position, speed in inputs:
    print(carFleet(target, position, speed))
