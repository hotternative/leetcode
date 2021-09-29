# Given a 1-indexed array of integers numbers that is
# already sorted in non-decreasing order, find two numbers such that
# they add up to a specific target number.
#
# Let these two numbers be numbers[index1] and numbers[index2]
# where 1 <= first < second <= numbers.length.
#
# Return the indices of the two numbers,
# index1 and index2, as an integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.

from typing import List
import unittest

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s > target:
                right -= 1
            else:
                left += 1


class TestSolutions(unittest.TestCase):
    def test1(self):
        s = Solution()
        numbers = [2,7,11,15]
        target = 9
        expected_output = [1,2]
        actual_output = s.twoSum(numbers, target)
        assert actual_output == expected_output

    def test2(self):
        s = Solution()
        numbers = [2,3,4]
        target = 6
        expected_output = [1,3]
        actual_output = s.twoSum(numbers, target)
        assert actual_output == expected_output

