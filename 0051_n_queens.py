from typing import List
from unittest import TestCase
from copy import copy

class Solution:
    @staticmethod
    def is_valid(c, track):
        if not track:
            return True

        for i in range(0, len(track)):
            # this is the fun bit, checking if the new entry attacks
            # existing ones diagonally in upper left and upper right direction
            if track[len(track) - i - 1] == c - i - 1 or track[len(track) - i - 1] == c + i + 1:
                return False
        return True

    @staticmethod
    def convert_solution(sols, n):
        """
        :param sols: list of solutions
        represented by location of queen at each row e.g. [[1, 3, 0, 2], [2, 0, 3, 1]]
        :return: queen position as requested by the problem, e.g. [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
        """
        final_sols = []
        for sol in sols:
            final_sol = []
            for v in sol:
                row = ["."] * n
                row[v] = "Q"
                row = "".join(row)
                final_sol.append(row)
            final_sols.append(final_sol)
        return final_sols

    def solveNQueens1(self, n: int) -> List[List[str]]:
        """While this works locally, it doesn't work on Leetcode"""
        sols = []

        def bt(track, choices):
            nonlocal sols

            if len(track) == n:
                sols.append(copy(track))
                print("append track: {}".format(track))
                return

            for c in choices:
                if Solution.is_valid(c, track):
                    track.append(c)
                    choices.remove(c)

                    bt(track, choices)

                    choices.add(c)
                    track.pop()

        track = []
        choices = set(range(n))
        bt(track, choices)

        return Solution.convert_solution(sols, n)


    def solveNQueens(self, n: int) -> List[List[str]]:
        """This works on Leetcode, difference being choices is copied"""
        sols = []

        def bt(track, choices):
            # print("calling bt with track: {}, choices: {}".format(track, choices))
            nonlocal sols

            if len(track) == n:
                # print("append track..")
                sols.append(copy(track))

                return

            temp_choices = copy(choices)
            for c in choices:

                if Solution.is_valid(c, track):
                    track.append(c)
                    temp_choices.remove(c)

                    bt(track, temp_choices)

                    temp_choices.add(c)
                    track.pop()

        track = []
        choices = set(range(n))
        bt(track, choices)

        return Solution.convert_solution(sols, n)

sols = Solution.solveNQueens(Solution, 8)
print(sols)
print(len(sols))
#
# class Test(TestCase):
#     def test_is_valid(self):
#         c = 0
#         track = [1, 3]
#         assert Solution.is_valid(c, track)
#
#         c = 1
#         track = [0,2]
#         assert not Solution.is_valid(c, track)
#
#         track = []
#         for c in range(4):
#             assert Solution.is_valid(c, track)