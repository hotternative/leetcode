# Created on 02/02/2021
from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = defaultdict(lambda: 0)
        for ball in range(lowLimit, highLimit+1):
            ball_str = str(ball)
            ball_sum = 0
            for c in ball_str:
                ball_sum += int(c)
            boxes[ball_sum] += 1

        return max(boxes.values())

print(Solution.countBalls(Solution, 4,10))


