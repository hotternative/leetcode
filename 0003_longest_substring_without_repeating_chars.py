"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", wtheme: minimatitle:ith the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 10**4
s consists of English letters, digits, symbols and spaces.

slow and fast
char map {char: index}
"""
import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Runtime: 36 ms, faster than 99.94% of Python3 online submissions.
        Memory Usage: 14.4 MB, less than 24.55% of Python3 online submissions.

        :param s:
        :return:
        """
        char_map = {}
        slow = fast = 0
        max_len = 0
        while fast < len(s):
            if s[fast] in char_map:
                for i in range(slow, char_map[s[fast]]+1):
                    del char_map[s[i]]
                    slow += 1
                char_map[s[fast]] = fast
            else:
                char_map[s[fast]] = fast
                if len(char_map) > max_len:
                    max_len = len(char_map)
            fast += 1
        return max_len

class TestSolution(unittest.TestCase):
    def test1(self):
        s = "abcabcbb"
        sol = Solution()
        assert sol.lengthOfLongestSubstring(s) == 3

    def test2(self):
        s = "bbbbb"
        sol = Solution()
        assert sol.lengthOfLongestSubstring(s) == 1

    def test3(self):
        s = "pwwkew"
        sol = Solution()
        assert sol.lengthOfLongestSubstring(s) == 3
