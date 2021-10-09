from typing import List
import collections
import unittest


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        l, r = 0, len(nums)-1
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                ans.append(nums[l]**2)
                l += 1
            else:
                ans.append(nums[r]**2)
                r -= 1
        return ans[::-1]

    def sortedSquares2(self, A):
        """
        O(N), 10 lines, beats 100%
        The question boils down to understanding that if we look at the magnitude
        of the elements in the array, A, both ends "slide down" and converge towards
         the center of the array.

         With that understanding, we can use two pointers, one at each end,
          to iteratively collect the larger square to a list.
          However, collecting the larger square in a list with list's append,
          results in elements sorted in descending order.

        To circumvent this, we need to append to the left of the list.
        Using a collections.deque() allows us to append elements to the left of answer in O(1) time,
        maintaining the required increasing order.
        https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100        :return:
        """
        answer = collections.deque()
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)

    def sortedSquares1(self, nums: List[int]) -> List[int]:
        """
        A reverse approach. First find i which is has the smallest absolute value,
        then deploy two pointers that slide towards the two ends of the array.
        :param nums:
        :return:
        """
        i = 0
        while i < len(nums)-1 and abs(nums[i]) >= abs(nums[i+1]):
            i += 1
        ans = [nums[i] ** 2]

        j = i - 1
        k = i + 1
        while k <= len(nums) - 1 and j >= 0:
            if abs(nums[j]) <= abs(nums[k]):
                ans.append(nums[j] ** 2)
                j -= 1
            else:
                ans.append(nums[k] ** 2)
                k += 1

        if j < 0:
            [ans.append(num ** 2) for num in nums[k:]]
        else:
            [ans.append(num ** 2) for num in nums[:j+1][::-1]]

        return ans


class TestSolution(unittest.TestCase):

    def test1(self):
        nums = [-4,-1,0,3,10]
        output = [0,1,9,16,100]
        s = Solution()
        assert s.sortedSquares(nums) == output

    def test2(self):
        nums = [-7,-3,2,3,11]
        output = [4,9,9,49,121]
        s = Solution()
        assert s.sortedSquares(nums) == output

    def test3(self):
        nums = [-5,-3,-2,-1]
        output = [1,4,9,25]
        s = Solution()
        assert s.sortedSquares(nums) == output