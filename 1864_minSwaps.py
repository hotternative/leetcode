import numpy as np
import pandas as pd
import unittest


class Solution:
    def minSwaps(self, s: str) -> int:
        n0, n1 = 0, 0
        for c in s:
            if c == '0':
                n0 += 1

        n1 = len(s) - n0

        if abs(n0 - n1) > 1:
            return -1

        ans = 1001


        if n0 >= n1: # start from 0
            swap_cnt = 0
            x = '0'
            for c in s:
                if c != x and c == '0':
                    swap_cnt += 1
                x = '1' if x == '0' else '0'

            if swap_cnt < ans:
                ans = swap_cnt

        if n0 <= n1:  # start from 0
            swap_cnt = 0
            x = '1'
            for c in s:
                if c != x and c == '0':
                    swap_cnt += 1
                x = '1' if x == '0' else '0'

            if swap_cnt < ans:
                ans = swap_cnt

        return ans

s = "111000"
print(Solution.minSwaps(Solution, s))

s = "010"
print(Solution.minSwaps(Solution, s))

s = "1110"
print(Solution.minSwaps(Solution, s))

s = "100"
print(Solution.minSwaps(Solution, s))

#
# class TestSolution(unittest.TestCase):
#     def test1(self):
#         assert 1 + 1 == 2
#
#
# if __name__ == '__main__':
#     unittest.main()


s = "111000"
n0, n1 = 3,3

