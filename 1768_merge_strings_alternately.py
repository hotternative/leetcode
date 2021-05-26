import numpy as np
import pandas as pd
import unittest
from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        [ans.extend((c, d)) for c, d in zip(word1, word2)]
        if len(word1) > len(word2):
            [ans.extend(c) for c in word1[(len(word2) - len(word1)):]]
        elif len(word2) > len(word1):
            [ans.extend(c) for c in word2[(len(word1) - len(word2)):]]
        return ''.join(ans)

class TestSolution(unittest.TestCase):
    def test1(self):
        word1 = "abc"
        word2 = "pqr"
        assert Solution.mergeAlternately(Solution, word1, word2) == "apbqcr"

    def test2(self):
        word1 = "ab"
        word2 = "pqrs"
        assert Solution.mergeAlternately(Solution, word1, word2) == "apbqrs"

    def test3(self):
        word1 = "abcd"
        word2 = "pq"
        assert Solution.mergeAlternately(Solution, word1, word2) == "apbqcd"


if __name__ == '__main__':
    unittest.main()