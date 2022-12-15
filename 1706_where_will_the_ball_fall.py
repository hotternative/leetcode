# 15 Dec 2022
# Runtime 439 ms Beats 59.5% Memory 14.5 MB Beats 34.75%

from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = []
        mp = {
            ('d', -1): 'l',
            ('d', 1): 'r',
            ('l', 1): 'r',
            ('r', -1): 'l',
            ('l', -1): 'd',
            ('r', 1): 'd',
        }

        for i in range(n):
            visited = [[False for _ in range(n)] for _ in range(m)]
            cur_dir = 'd'
            row, col = 0, i
            while True:
                visited[row][col] = True
                cur_bd = grid[row][col]
                next_dir = mp[(cur_dir, cur_bd)]
                if next_dir == 'l':
                    col -= 1
                elif next_dir == 'r':
                    col += 1
                else:  # going down
                    row += 1

                cur_dir = next_dir
                if row >= m:
                    res.append(col)
                    break
                if col < 0 or col >= n or visited[row][col]:
                    res.append(-1)
                    break

        return res



import unittest
class TestSolutions(unittest.TestCase):
    def test1(self):
        s = Solution()
        result = s.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]])
        assert result == [1,-1,-1,-1,-1]


    def test2(self):
        s = Solution()
        result = s.findBall([[-1]])
        assert result == [-1]

    def test3(self):
        s = Solution()
        result = s.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]])
        assert result == [0,1,2,3,4,-1]






