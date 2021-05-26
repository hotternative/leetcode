from bisect import bisect_left, insort
from typing import List

nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]
# [5, 10, 10, 20, 100]
# --> bisect_left(55) --> 4  --> len(nums2) - 4 - 1 = 0  (1-0 = 1)
# --> bisect_left(5)  --> 0  --> len(nums2) - 0  -1 = 4  (4-2 = 2)

print(bisect_left(nums2[::-1], 5))
insort(nums2[::-1], 5)
print(nums2)
#
# class Solution:
#     def maxDistance(self, nums1: List[int], nums2: List[int]):
#         n2b = nums2[::-1]
#
#         md = 0
#
#         for i, n in enumerate(nums1):
#             d = (len(nums2) - bisect_left(n2b, n) - 1) - i
#
#             if d > md:
#                 md = d
#
#         return md
#
#
# nums1 = [2,2,2]
# nums2 = [10,10,1]
# ans = Solution.maxDistance(Solution, nums1, nums2)
# print(ans)
#
# nums1 = [30,29,19,5]
# nums2 = [25,25,25,25,25]
# ans = Solution.maxDistance(Solution, nums1, nums2)
# print(ans)
#
#
# nums1 = [5,4]
# nums2 = [3,2]
# ans = Solution.maxDistance(Solution, nums1, nums2)
# print(ans)
