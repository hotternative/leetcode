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

        if k == 0:
            return
        k = k % len(nums)
        temp = nums[len(nums)-k:]
        nums[k:] = nums[:len(nums)-k]
        nums[:k] = temp

    def rotate2(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        if k == 0:
            return
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:n-k]

    def rotate3(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        if k == 0:
            return
        n = len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]

    def rotate(self, nums: List[int], k: int) -> None:
        # Runtime: 216 ms, faster than 80.87% of Python3 online submissions
        # Memory Usage: 25.6 MB, less than 12.51% of Python3 online submissions.
        k = k % len(nums)
        if k == 0:
            return
        nums[:k], nums[k:] = nums[-k:], nums[:-k]

class TestSolution(unittest.TestCase):

    methods_to_test = [func for func in dir(Solution) if callable(getattr(Solution, func)) and not func.startswith('__')]
    s = Solution()

    def test1(self):
        for method in TestSolution.methods_to_test:
            nums = [1,2,3,4,5,6,7]
            k = 3
            output = [5,6,7,1,2,3,4]
            method_to_test = getattr(self.s, method)
            method_to_test(nums, k)
            assert nums == output

    def test2(self):
        for method in TestSolution.methods_to_test:
            nums = [-1,-100,3,99]
            k = 2
            expected_output = [3,99,-1,-100]
            method_to_test = getattr(self.s, method)
            method_to_test(nums, k)
            assert nums == expected_output

    def test3(self):
        for method in TestSolution.methods_to_test:
            nums = [1]
            k = 0
            expected_output = [1]
            method_to_test = getattr(self.s, method)
            method_to_test(nums, k)
            assert nums == expected_output