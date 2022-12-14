from typing import List
import unittest

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [1,3,5,6]
        target = 5
        output = 2
        s = Solution()
        assert s.searchInsert(nums, target) == output

    def test2(self):
        nums = [1,3,5,6]
        target = 2
        output = 1
        s = Solution()
        assert s.searchInsert(nums, target) == output

    def test3(self):
        nums = [1,3,5,6]
        target = 7
        output = 4
        s = Solution()
        assert s.searchInsert(nums, target) == output

    def test4(self):
        nums = [1,3,5,6]
        target = 0
        output = 0
        s = Solution()
        assert s.searchInsert(nums, target) == output

    def test5(self):
        nums = [1]
        target = 0
        output = 0
        s = Solution()
        assert s.searchInsert(nums, target) == output

