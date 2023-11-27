from typing import Dict, List, Set, Tuple

class Solution:
    # Runtime 543 ms Beats 7.10% Memory 14.2 MB Beats 5.21%

    def dfs(self, counter: Dict, s: int):

        if s == self.target:
            self.results.add(tuple([(k, v) for k, v in counter.items()]))
            return

        for candidate in self.candidates:
            if s + candidate <= self.target:
                counter[candidate] += 1
                s += candidate

                self.dfs(counter, s)

                counter[candidate] -= 1
                s -= candidate

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results: Set[Tuple] = set()
        self.candidates = candidates
        self.target = target
        counter, s = {candidate: 0 for candidate in candidates}, 0
        self.dfs(counter, s)

        ans = [[k for k, v in result for _ in range(v)] for result in self.results]
        return ans




import unittest
class TestSolution(unittest.TestCase):

    def test1(self):
        candidates = [2,3,6,7]
        target = 7

        s = Solution()
        ans = s.combinationSum(candidates, target)
        assert [7] in ans
        assert [2,2,3] in ans

    def test2(self):
        candidates = [2,3,5]
        target = 8

        s = Solution()
        actual_ans = s.combinationSum(candidates, target)
        expected_ans = [[2,2,2,2],[2,3,3],[3,5]]
        for ans in expected_ans:
            assert ans in actual_ans
