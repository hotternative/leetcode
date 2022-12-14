import math
from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(lambda:0)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                p = nums[i] * nums[j]
                # print(i,j)
                d[p] += 1
        # print(d)
        ans = 0
        for v in d.values():
            if v > 1:
                ans += math.factorial(v) / (2 * math.factorial(v-2))

        return int(ans * 8)


nums = [1,2,4,5,10]
print(Solution.tupleSameProduct(Solution, nums))


nums = [2,3,4,6,8,12]
print(Solution.tupleSameProduct(Solution, nums))

nums = [2,3,5,7]
print(Solution.tupleSameProduct(Solution, nums))