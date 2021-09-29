from typing import List
import unittest

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        The easiest way is to use the built-in reverse method
        """
        s.reverse()

    def reverseString1(self, s: List[str]) -> None:
        """
        Two pointers
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

class TestSolution(unittest.TestCase):
    methods_to_test = [
        func for func in dir(Solution) if callable(getattr(Solution, func)) and not func.startswith('__')]

    def test1(self):

        for method in TestSolution.methods_to_test:
            sol = Solution()
            s = ["h","e","l","l","o"]
            expected_output = ["o","l","l","e","h"]
            method_to_test = getattr(sol, method)
            method_to_test(s)
            assert s == expected_output