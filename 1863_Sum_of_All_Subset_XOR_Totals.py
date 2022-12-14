from typing import List
from itertools import combinations, accumulate
from functools import reduce

class Solution:
    def subsetXORSum2(self, nums: List[int]) -> int:
        """making use of the built in combinations function and the accumulate function"""

        # Runtime: 108 ms, faster than 42.20% of Python3 online submissions for Sum of All Subset XOR Totals.
        # Memory Usage: 14.2 MB, less than 84.97% of Python3 online submissions for Sum of All Subset XOR Totals.
        sm = 0
        for i in range(1, len(nums)+1):
            for c in combinations(nums, i):
                # print('computing {}...'.format(c))
                s = list(accumulate(c, lambda x, y: x ^ y))[-1]
                # print('xor result is: {}'.format(s))
                sm += s

        return sm


    def subsetXORSum3(self, nums: List[int]) -> int:
        """making use of the built in combinations function and the reduce func"""
        # Runtime: 88 ms, faster than 58.12% of Python3 online submissions for Sum of All Subset XOR Totals.
        # Memory Usage: 14.4 MB, less than 26.61% of Python3 online submissions for Sum of All Subset XOR Totals.

        # observation: combinations is more memory efficient than reduce

        sm = 0
        for i in range(1, len(nums)+1):
            for c in combinations(nums, i):
                # print('computing {}...'.format(c))
                s = reduce(lambda x, y: x ^ y, c)
                # print('xor result is: {}'.format(s))
                sm += s

        return sm

    def subsetXORSum(self, nums: List[int]) -> int:
        """making use of recursion"""
        # Runtime: 76 ms, faster than 67.69% of Python3 online submissions for Sum of All Subset XOR Totals.
        # Memory Usage: 14 MB, less than 94.77% of Python3 online submissions for Sum of All Subset XOR Totals.
        sm = 0

        def bt(seed, rn):
            nonlocal sm
            if not rn:
                return

            bt(seed, rn[1:])

            x = seed^rn[0]
            sm += x
            bt(x, rn[1:])

        bt(0, nums)

        return sm




nums = [1,3]
print(Solution.subsetXORSum(Solution, nums))

# nums = [2, 5, 6]
nums = [5, 1, 6]
print(Solution.subsetXORSum(Solution, nums))

nums = [3,4,5,6,7,8]
print(Solution.subsetXORSum(Solution, nums))

# from functools import reduce
# x = reduce(lambda x, y: x ^ y, nums)

# print(x)
#
# print(0 ^ 0)  # -->0
# print(1 ^ 0)  # -->1
# print(0 ^ 1)  # -->1
# print(1 ^ 1)  # -->0
#
# there is no xor built-in function
# print(xor(0, 0))
# print(xor(1, 0))
# print(xor(0, 1))
# print(xor(1, 1))

print(type(combinations([1,2,3],2)))