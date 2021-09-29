"""
Given a string s, reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

1 <= s.length <= 5 * 10**4
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.

"""
import unittest

class Solution:
    def reverseWords(self, s: str) -> str:
        # Runtime: 36 ms, Memory Usage: 14.7 MB
        return ' '.join(w[::-1] for w in s.split(' '))

    def reverseWords_two_pointers(self, s: str) -> str:
        # Runtime: 148 ms, Memory Usage: 15.2 MB

        s = list(s)
        i = j = k = 0  # i: start of a word, j: current head location, k: end of a word
        while j < len(s):
            if s[j] == ' ':
                k -= 1
                while i < k:
                    s[k], s[i] = s[i], s[k]
                    i += 1
                    k -= 1
                i = k = j + 1

            elif j == len(s) - 1:
                k = j
                while i < k:
                    s[k], s[i] = s[i], s[k]
                    i += 1
                    k -= 1

            else:
                k = j + 1

            j += 1

        return ''.join(s)

class TestSolution(unittest.TestCase):
    methods_to_test = [
        func for func in dir(Solution) if callable(getattr(Solution, func)) and not func.startswith('__')]

    def test1(self):
        s = "Let's take LeetCode contest"
        sol = Solution()
        expected_output = "s'teL ekat edoCteeL tsetnoc"
        for method in TestSolution.methods_to_test:
            method_to_test = getattr(sol, method)
            actual_output = method_to_test(s)
            assert actual_output == expected_output

    def test2(self):
        s = "God Ding"
        sol = Solution()
        expected_output = "doG gniD"
        for method in TestSolution.methods_to_test:
            method_to_test = getattr(sol, method)
            actual_output = method_to_test(s)
            assert actual_output == expected_output

