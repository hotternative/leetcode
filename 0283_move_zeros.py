from typing import List
import unittest

# Given an integer array nums,
# move all 0's to the end of it while maintaining the relative order
# of the non-zero elements.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head, tail = 0, None # head for where it's looking at, tail for the last zero position
        while head < len(nums):
            if nums[head] == 0:
                if tail is None:
                    tail = head
            else:
                if tail is not None:
                    nums[tail] = nums[head]
                    nums[head] = 0
                    tail += 1
            head += 1

class TestSolutions(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [0,1,0,3,12]
        expected_output = [1,3,12,0,0]
        s.moveZeroes(nums)
        assert nums == expected_output

    def test2(self):
        s = Solution()
        nums = [0]
        expected_output = [0]
        s.moveZeroes(nums)
        assert nums == expected_output
