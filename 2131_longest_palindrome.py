from typing import Dict, List
import unittest


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # Runtime 1444 ms Beats 46.47% Memory 38.3 MB Beats 54.13%
        res = 0
        not_paired_diff: Dict[str, int] = dict()
        not_paired_same = set()

        for word in words:
            if word[0] == word[1]:
                if word in not_paired_same:
                    res += 4
                    not_paired_same.remove(word)
                else:
                    not_paired_same.add(word)

            else:
                mirror = word[1] + word[0]

                if mirror in not_paired_diff and not_paired_diff[mirror] > 0:
                    not_paired_diff[mirror] -= 1
                    res += 4
                    if not_paired_diff[mirror] == 0:
                        not_paired_diff.pop(mirror)
                else:
                    if word in not_paired_diff:
                        not_paired_diff[word] += 1
                    else:
                        not_paired_diff[word] = 1
        if not_paired_same:
            res += 2

        return res


# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/solutions/2772466/python-solution-hash-map-approach/

class TestSolutions(unittest.TestCase):
    def test1(self):
        s = Solution()
        words = ["lc", "cl", "gg"]
        assert s.longestPalindrome(words) == 6

    def test2(self):
        s = Solution()
        words = ["ab", "ty", "yt", "lc", "cl", "ab"]
        assert s.longestPalindrome(words) == 8

    def test3(self):
        s = Solution()
        words = ["cc", "ll", "xx"]
        assert s.longestPalindrome(words) == 2

    def test4(self):
        s = Solution()

        words = ["qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"]

        assert s.longestPalindrome(words) == 14



