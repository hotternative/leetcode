"""
"""
from typing import List
from collections import Counter
import unittest

class Solution:
    # Runtime 393 ms Beats 91.43% Memory 14.2 MB Beats 84.91%
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        sorted_c = sorted(c.items(), key=lambda x:x[1])
        t, m = c.most_common(1)[0]
        r = 0
        for item in sorted_c:
            if item[1] == m:
                r += 1
        return max((m - 1) * (n + 1) + r, len(tasks))



class TestSolutions(unittest.TestCase):
    def test1(self):
        s = Solution()
        tasks = ["A","A","A","B","B","B"]
        n = 0
        assert s.leastInterval(tasks, n) == 6