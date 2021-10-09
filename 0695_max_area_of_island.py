"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

loop each row and each column
if land, dfs
"""
import unittest
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Runtime: 120 ms, faster than 98.03% of Python3 online submissions for Max Area of Island.
        Memory Usage: 17 MB, less than 37.91% of Python3 online submissions for Max Area of Island.
        :param grid:
        :return:
        """
        max_land = 0

        def dfs(i, j):
            nonlocal land
            if i - 1 >= 0 and grid[i-1][j]:
                land += 1
                grid[i-1][j] = 0
                dfs(i-1, j)

            if i + 1 < len(grid) and grid[i+1][j]:
                land += 1
                grid[i+1][j] = 0
                dfs(i+1, j)

            if j - 1 >= 0 and grid[i][j-1]:
                land += 1
                grid[i][j-1] = 0
                dfs(i, j-1)

            if j + 1 < len(grid[0]) and grid[i][j+1]:
                land += 1
                grid[i][j+1] = 0
                dfs(i, j+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    land = 1
                    dfs(i, j)
                    # new found land!
                    if land > max_land:
                        max_land = land

        return max_land

class TestSolution(unittest.TestCase):
    def test1(self):
        grid = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
        sol = Solution()
        expected_output = 6
        actual_result = sol.maxAreaOfIsland(grid)
        assert actual_result == expected_output

    def test2(self):
        grid = [[0,0,0,0,0,0,0,0]]
        sol = Solution()
        expected_output = 0
        actual_result = sol.maxAreaOfIsland(grid)
        assert actual_result == expected_output


