# 15 Dec 2022
# Runtime 27 ms Beats 99.17% Memory 13.9 MB Beats 73.87%

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(num:str):
            s = 0
            l = len(num)
            for i, c in enumerate(num):
                s += 10 ** (l-i-1) * int(c)
            return s

        return str(convert(num1) * convert(num2))