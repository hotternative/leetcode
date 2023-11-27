from typing import List, Tuple

"""
    def dfs(路径, 选择列表):
        if 满足结束条件:
            result.add(路径)
            return

        for 选择 in 选择列表:
            做选择
            dfs(路径, 选择列表)
            撤销选择
"""


class Solution:
    # Runtime 7050 ms Beats 60.11% Memory 14.1 MB Beats 10.41%
    def find_new_choices(self, path, choice):
        new_choices = []
        i, j = choice
        new_char = self.word[len(path)]
        if i - 1 >= 0 and self.visited[i-1][j] == 0 and self.board[i-1][j] == new_char:
            new_choices.append((i-1, j))
        if j - 1 >= 0 and self.visited[i][j-1] == 0 and self.board[i][j-1] == new_char:
            new_choices.append((i, j-1))
        if i + 1 < self.m and self.visited[i+1][j] == 0 and self.board[i+1][j] == new_char:
            new_choices.append((i+1, j))
        if j + 1 < self.n and self.visited[i][j+1] == 0 and self.board[i][j+1] == new_char:
            new_choices.append((i, j+1))
        return new_choices


    def backtrack(self, path: List[Tuple[int, int]], choices: List[Tuple[int, int]]):

        for choice in choices:
            path.append(choice)
            if len(path) == len(self.word):
                return True
            new_choices = self.find_new_choices(path, choice)
            i, j = choice
            self.visited[i][j] = 1
            res = self.backtrack(path, new_choices)
            if res:
                return True
            self.visited[i][j] = 0
            path.pop()


    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = list(word)
        self.board = board
        self.m, self.n = len(board), len(board[0])
        self.visited = [[0] * self.n for i in range (self.m)]
        choices = []
        path = []
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == self.word[0]:
                    choices.append((i, j))
        if self.backtrack(path, choices):
            return True
        else:
            return False


import unittest
class TestSolution(unittest.TestCase):

    def test1(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        s = Solution()
        assert s.exist(board, word)

    def test2(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "SEE"
        s = Solution()
        assert s.exist(board, word)

    def test3(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCB"
        s = Solution()
        assert not s.exist(board, word)



