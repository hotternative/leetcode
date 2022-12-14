# 14 Dec 2022
# Runtime 34 ms Beats 89.11%
# Memory 14.1 MB Beats 34.83%
from typing import List, NamedTuple


class Loc(NamedTuple):
    row: int
    col: int


class Solution:
    def find_next(self, cur: Loc) -> Loc:
        if self.cur_dir == "r":
            next_loc = Loc(row=cur.row, col=cur.col + 1)
        elif self.cur_dir == "d":
            next_loc = Loc(row=cur.row + 1, col=cur.col)
        elif self.cur_dir == "l":
            next_loc = Loc(row=cur.row, col=cur.col - 1)
        else:
            next_loc = Loc(row=cur.row - 1, col=cur.col)
        return next_loc

    def is_valid_loc(self, next_loc: Loc) -> bool:
        if (
            next_loc.row >= self.m
            or next_loc.col >= self.n
            or self.visited[next_loc.row][next_loc.col]
        ):
            return False
        else:
            return True

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res: List[int] = []
        cur_loc = Loc(row=0, col=0)
        self.direction_transition = {"r": "d", "d": "l", "l": "u", "u": "r"}
        self.cur_dir = "r"
        self.m, self.n = len(matrix), len(matrix[0])

        self.visited: List[List[bool]] = [[False for i in range(self.n)] for j in range(self.m)]

        while True:
            res.append(matrix[cur_loc.row][cur_loc.col])

            self.visited[cur_loc.row][cur_loc.col] = True

            next_loc = self.find_next(cur_loc)

            if self.is_valid_loc(next_loc):
                cur_loc = next_loc
            else:
                self.cur_dir = self.direction_transition[self.cur_dir]
                next_loc = self.find_next(cur_loc)
                if not self.is_valid_loc(next_loc):
                    break
                else:
                    cur_loc = next_loc

        return res


import unittest
class TestSolutions(unittest.TestCase):
    def test1(self):
        s = Solution()
        result = s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
        assert result == [1,2,3,6,9,8,7,4,5]
