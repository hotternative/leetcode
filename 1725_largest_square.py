# Created on 05/02/2021
from typing import List
from collections import defaultdict
class Solution1:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        c = defaultdict(lambda:0)
        for r in rectangles:
            s = min(r)
            c[s] += 1
        print(c)

        maxLen = 0
        ans = 0
        for l, n in c.items():
            if l > maxLen:
                ans = n
                maxLen = l
        return ans

from collections import Counter
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        s = [min(r) for r in rectangles]
        c = Counter(s)
        print(c)

rectangles = [[2,3],[3,7],[4,3],[3,7]]
print(Solution.countGoodRectangles(Solution, rectangles))

rectangles = [[5,8],[3,9],[5,12],[16,5]]
print(Solution.countGoodRectangles(Solution, rectangles))