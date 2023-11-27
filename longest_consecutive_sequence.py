from typing import Dict, List, Set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for n in nums:
            if n in nums_set:

            visited[n] = {n}
            if n - 1 in visited:
                visited[n-1].add(n)
                visited[n] = visited[n-1]

            if n + 1 in visited:
                temp = visited[n+1]
                visited[n] = visited[n+1]
                visited[n].update(temp)

            if len(visited[n]) > ans:
                ans = len(visited[n])

        return ans

import unittest
class TestSolution(unittest.TestCase):

    def test1(self):
        nums = [100,4,200,1,3,2]
        expected_output = 4

        s = Solution()
        ans = s.longestConsecutive(nums)

        assert ans == expected_output
