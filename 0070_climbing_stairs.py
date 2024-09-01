class Solution:
    solved = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.solved:
            return self.solved[n]
        ans = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.solved[n] = ans
        return ans



import unittest
class TestSolutions(unittest.TestCase):
    def test1(self):
        s = Solution()
        result = s.climbStairs(2)
        assert result == 2

    def test2(self):
        s = Solution()
        result = s.climbStairs(3)
        assert result == 3