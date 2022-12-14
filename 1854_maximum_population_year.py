from typing import List
from collections import defaultdict

class Solution:
    def maximumPopulation(self, logs: List[List[int]]):
        p = {i:0 for i in range(1950, 2050)}

        for log in logs:
            s, e = log[0], log[1]
            for y in range(s, e):
                p[y] += 1

        print(p)
        m = -1
        ey = 1950
        for k, v in p.items():
            if v > m:
                ey = k
                m = v

        return ey


i = [[1993,1999],[2000,2010]]
ans = Solution.maximumPopulation(Solution, i)
print(ans)