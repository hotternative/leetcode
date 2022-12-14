from typing import List
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:

        # ps = [0] * len(nums)
        ps = []
        s = 0
        for n in nums:
            s += n
            ps.append(s)

        st = []  # monotonic-increasing stack
        la = []  # la[i] stores the index of the nearest smaller element on the left of n[i]
        for i, n in enumerate(nums):
            while st and nums[st[-1]] >= n:
                st.pop()

            la.append(st[-1]) if st else la.append(-1)
            st.append(i)
        # print(la)

        st = []  # monotonic-increasing stack
        ra = []  # ra[i] stores the index of the nearest smaller element on the right of n[i]
        for i in range(len(nums)-1, -1, -1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()

            ra.append(st[-1]) if st else ra.append(len(nums))
            st.append(i)
        ra.reverse()

        ans = 0

        for i, n in enumerate(nums):
            rs = ps[ra[i]-1]
            ls = ps[la[i]] if la[i] >= 0 else 0
            ans = max(ans, (rs-ls)*n)
        return ans


    def maxSumMinProduct_O_N2(self, nums: List[int]) -> int:
        ms = 0
        for i, n in enumerate(nums):

            s = n

            l = i - 1
            r = i + 1

            while l >= 0 and nums[l] > n:
                s += nums[l]
                l -= 1

            while r < len(nums) and nums[r] >= n:
                s += nums[r]
                r += 1

            if n * s > ms:
                ms = n * s

        return ms % (10 ** 9 + 7)


nums = [1,2,3,2]
ans = Solution.maxSumMinProduct(Solution, nums)
assert ans == 14 # Output: 14

nums = [2,3,3,1,2]
ans = Solution.maxSumMinProduct(Solution, nums)
print(ans)# Output: 18

nums = [3, 1, 5, 6, 4, 2]
ans = Solution.maxSumMinProduct(Solution, nums)
print(ans)# Output: 60
