from typing import List

class Solution:

    def rob1(self, nums: List[int]) -> int:
        # Runtime 33 ms Beats 68.23% Memory 13.9 MB Beats 13.69%
        if len(nums) == 1:
            return nums[0]

        i = 2

        answers = [nums[0], max(nums[0], nums[1])]

        while i < len(nums):
            answers.append(
                max(
                    answers[i - 2] + nums[i],
                    answers[i - 1])
            )
            i += 1
        return answers[-1]

    def rob(self, nums: List[int]) -> int:
        # Runtime 43 ms Beats 15% Memory 13.9 MB Beats 55.75%
        if len(nums) == 1:
            return nums[0]

        i = 2

        prev_ans, ans = nums[0], max(nums[0], nums[1])
        while i < len(nums):
            new_ans = max(prev_ans + nums[i], ans)
            prev_ans, ans = ans, new_ans
            i += 1
        return ans
