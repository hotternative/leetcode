from typing import List
import collections
import unittest


class Solution:
    """
        Do not return anything, modify nums in-place instead
    """
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        easiest solution would use additional memory
        """
        k = k % len(nums)
        temp = nums[len(nums)-k:]
        nums[k:] = nums[:len(nums)-k]
        nums[:k] = temp

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]

class TestSolution(unittest.TestCase):

    methods_to_test = [func for func in dir(Solution) if callable(getattr(Solution, func)) and not func.startswith('__')]

    def test1(self):
        for method in TestSolution.methods_to_test:
            nums = [1,2,3,4,5,6,7]
            k = 3
            output = [5,6,7,1,2,3,4]
            s = Solution()
            method_to_test = getattr(s, method)
            method_to_test(nums, k)
            assert nums == output

    def test2(self):
        for method in TestSolution.methods_to_test:
            nums = [-1,-100,3,99]
            k = 2
            output = [3,99,-1,-100]
            s = Solution()
            s.rotate(nums, k)

            assert nums == output
