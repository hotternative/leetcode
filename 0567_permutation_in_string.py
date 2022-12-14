"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

# 1. we need a counter for s1
#
# slow and fast pointer
# 2. we need a {char: [locs]} for sliding window,
# we also maintain a total_char for the sliding window

# if fast not in counter, slow = fast  = fast + 1: reset {} and total char
# if fast in counter:
#     if number of char < counter:
#          add it in
#           if total char == target: return True
#     else:
#       pop the earliest char and anything between slow and the earliest
#       maintain slow and total_char
# return false

from collections import Counter, defaultdict, deque
import unittest

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_count = Counter(s1)
        target = len(s1)
        total_char = 0
        slow = fast = 0
        window_memo = defaultdict(deque)
        while fast < len(s2):
            cur_char = s2[fast]
            if cur_char in s_count:
                if len(window_memo[cur_char]) < s_count[cur_char]:
                    total_char += 1
                    window_memo[cur_char].append(fast)
                    if total_char == target:
                        return True
                else:
                    # number of cur_char has already reached the desired length
                    earliest = window_memo[cur_char][0]
                    total_char = total_char - (earliest - slow)
                    for i in range(slow, earliest + 1):
                        window_memo[s2[i]].popleft()
                    slow = earliest + 1
                    window_memo[cur_char].append(fast)
            else:
                window_memo = defaultdict(deque)
                slow = fast + 1
                total_char = 0
            fast += 1
        return False

class TestSolution(unittest.TestCase):
    def test_check_inclusion1(self):
        s1 = "ab"
        s2 = "eidbaooo"
        sol = Solution()
        assert sol.checkInclusion(s1, s2)

    def test_check_inclusion2(self):
        s1 = "ab"
        s2 = "eidboaoo"
        sol = Solution()
        assert not sol.checkInclusion(s1, s2)

    def test_check_3(self):
        s1 = "adc"
        s2 = "dcda"
        sol = Solution()
        assert sol.checkInclusion(s1, s2)

    def test_4(self):
        s1 = "hello"
        s2 = "ooolleoooleh"
        sol = Solution()
        assert not sol.checkInclusion(s1, s2)