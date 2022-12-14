from typing import List
from bisect import bisect_left
import unittest


class Solution:
    """
    A solution using labuladong's binary search framework
    https://leetcode-cn.com/problems/binary-search/solution/er-fen-cha-zhao-xiang-jie-by-labuladong/
    """
    def search(self, nums: List[int], target: int):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
        return -1

class Solution1:
    """
    A test using the built-in binary search library.
    Unfortunately this doesn't work because it returns the leftmost one which is greater than target.
    """
    def search(self, nums: List[int], target: int):
        return bisect_left(nums, target)

class TestSolutions(unittest.TestCase):
    Solutions = (
        # Solution1,
        Solution,
    )

    # @unittest.skip('test')
    def test1(self):
        nums = [-1,0,3,5,9,12]
        target = 9
        output = 4
        for Solution in TestSolutions.Solutions:
            s = Solution()
            assert s.search(nums, target) == output

    def test2(self):
        nums = [-1,0,3,5,9,12]
        target = 2
        output = -1
        for Solution in TestSolutions.Solutions:
            s = Solution()
            assert s.search(nums, target) == output
            # print(s.search(nums, target))