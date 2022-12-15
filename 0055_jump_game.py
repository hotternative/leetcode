from typing import List

# 15 Dec
# Runtime 585 ms Beats 80.18% Memory 15.4 MB Beats 5.88%
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        reached = 0
        cur_idx = 0
        indice_to_check: list = [cur_idx]

        while indice_to_check:

            end_to_check = cur_idx + nums[cur_idx]
            indice_to_check.extend(range(reached + 1, end_to_check + 1))
            reached = max(reached, end_to_check)
            if reached >= len(nums) - 1:
                return True

            cur_idx = indice_to_check.pop()

        return False


import unittest
class TestSolutions(unittest.TestCase):
    def test1(self):
        s = Solution()
        result = s.canJump([2,3,1,1,4])
        assert result

    def test2(self):
        s = Solution()
        result = s.canJump([3,2,1,0,4])
        assert not result

    def test3(self):
        s = Solution()
        result = s.canJump([0, 1])
        assert not result

    def test4(self):
        s = Solution()
        result = s.canJump([1,2,3])
        assert result
