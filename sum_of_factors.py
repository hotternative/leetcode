from typing import List
import unittest

def sums_of_factors_basic(nums: List[int]) -> List[int]:
    ans = []
    for n in nums:
        s = 0
        for i in range(1, n//2 + 1):
            if n % i == 0:
                s += i
        ans.append(s)
    return ans

def sums_of_factors_improved(nums: List[int]) -> List[int]:
    ans = []
    for n in nums:
        s = 1
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                s += i
                j = n//i
                if i != j:
                    s += j
        ans.append(s)
    return ans


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [6, 8, 12]
        sol = sums_of_factors_improved(nums)
        print(sol)
        assert sol == [6, 7, 16]