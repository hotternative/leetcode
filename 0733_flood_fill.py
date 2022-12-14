"""
An image is represented by an m x n integer grid image where image[i][j]
represents the pixel value of the image.

You are also given three integers sr, sc, and newColor.
You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel,
plus any pixels connected 4-directionally to the starting pixel
of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels (also with the same color),
and so on.

Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Constraints:
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n

start from sr, sc.
if same color already, do nothing
else find neighbours with original color, paint it with new color.
"""
import unittest
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Runtime: 64 ms, faster than 99.07% of Python3 online submissions for Flood Fill.
        Memory Usage: 14.6 MB, less than 9.83% of Python3 online submissions for Flood Fill.
        :param image:
        :param sr:
        :param sc:
        :param newColor:
        :return:
        """
        original_color = image[sr][sc]

        def dfs(sr, sc):
            if sr + 1 < len(image) and image[sr+1][sc] == original_color:
                image[sr+1][sc] = newColor
                dfs(sr+1, sc)
            if sr - 1 >= 0 and image[sr-1][sc] == original_color:
                image[sr-1][sc] = newColor
                dfs(sr-1, sc)
            if sc + 1 < len(image[0]) and image[sr][sc+1] == original_color:
                image[sr][sc+1] = newColor
                dfs(sr, sc+1)
            if sc -1 >= 0 and image[sr][sc-1] == original_color:
                image[sr][sc-1] = newColor
                dfs(sr, sc-1)

        if newColor != original_color:
            image[sr][sc] = newColor
            dfs(sr, sc)
        return image

class TestSolution(unittest.TestCase):
    def test1(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1
        sc = 1
        newColor = 2
        sol = Solution()
        expected_output = [[2,2,2],[2,2,0],[2,0,1]]
        assert sol.floodFill(image, sr, sc, newColor) == expected_output
    def test2(self):
        image = [[0,0,0],[0,0,0]]
        sr = 0
        sc = 0
        newColor = 2
        sol = Solution()
        expected_output = [[2,2,2],[2,2,2]]
        assert sol.floodFill(image, sr, sc, newColor) == expected_output


