import numpy as np
import pandas as pd
import unittest
from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(c) for c in boxes]

        l = 0
        cl = 0
        r = 0
        cr = 0

        for i in range(1, len(boxes)):
            if boxes[i]:
                r += i
                cr += 1
        ans = []
        ans.append(l+r)

        for p in range(1, len(boxes)):
            r = r - cr
            l = l + cl + boxes[p-1]
            if boxes[p]:
                cr -= 1
            if boxes[p-1]:
                cl += 1
            ans.append(l+r)

        return ans



class TestSolution(unittest.TestCase):
    def test1(self):
        boxes = "110"
        assert Solution.minOperations(Solution, boxes) == [1, 1, 3]

    def test2(self):
        boxes = "001011"
        assert Solution.minOperations(Solution, boxes) == [11,8,5,4,3,4]


if __name__ == '__main__':
    unittest.main()