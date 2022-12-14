class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()
        next_val = n

        while next_val not in visited:
            visited.add(next_val)
            cur_val = next_val
            next_val = 0
            for char in str(cur_val):
                print(char)
                next_val += (int(char)) ** 2
            print(f"next_val: {next_val}")
            if next_val == 1:
                return True

        return False


import unittest
class TestSolutions(unittest.TestCase):
    def test1(self):
        s = Solution()
        result = s.isHappy(19)
        assert result

    def test2(self):
        s = Solution()
        result = s.isHappy(2)
        assert not result