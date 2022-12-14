from typing import List
from bisect import bisect_left
import unittest

class SolutionBase():
    def __init__(self, bad):
        self.bad = bad
    def isBadVersion(self, version):
        return version >= self.bad

class Solution(SolutionBase):
    """
    """
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo < hi:  # to check
            mid = lo + (hi - lo) // 2
            if self.isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi


class TestSolutions(unittest.TestCase):
    def test1(self):
        s = Solution(4)
        assert s.firstBadVersion(5) == 4

    def test2(self):
        s = Solution(4)
        assert s.firstBadVersion(5000000) == 4

    def test3(self):
        s = Solution(1)
        assert s.firstBadVersion(1) == 1
