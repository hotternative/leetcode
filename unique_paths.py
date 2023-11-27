from typing import Optional
import unittest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Runtime 31 ms Beats 79% Memory 13.8 MB Beats 66.10%
        ans = [1] * n
        i, j = 1, 0

        while i < m:
            while j < n:
                if j == 0:
                    j += 1
                    continue
                ans[j] = ans[j] + ans[j - 1]
                j += 1
            j = 0
            i += 1
        return ans[-1]


class TestSolution(unittest.TestCase):

    def test1(self):
        m, n = 3, 2
        s = Solution()
        assert s.uniquePaths(m, n) == 3


