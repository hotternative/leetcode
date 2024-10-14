from typing import List


class Solution:
    # Naive approach. Time complexity: O(n * log(n))
    # Runtime 181 ms Beats 5.02% Analyze Complexity Memory 23.22 MB Beats 45.13%
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            binary_str = bin(i)[2:]
            binary_int_list = [int(c) for c in binary_str]
            ans.append(sum(binary_int_list))
        return ans


class Solution2:
    # Dynamic building the next block. Time complexity: O(n)

    # Runtime 61 ms Beats 66.58% Analyze Complexity Memory 23.23 MB Beats 45.13%

    # 0 --> 0
    # 1 --> 1

    # 2 --> 10
    # 3 --> 11

    # 4 --> 100
    # 5 --> 101
    # 6 --> 110
    # 7 --> 111

    # 8 --> 1000
    # 9 --> 1001
    # 10 --> 1010
    # 11 --> 1011
    # 12 --> 1100
    # 13 --> 1101
    # 14 --> 1110
    # 15 --> 1111

    # (0, 1,        1, 2,      1, 2, 2, 3,    1, 2, 2, 3, 2, 3, 3, 4)
    # (2**0,        2**1,       2**2,                 2**3)

    def countBits(self, n: int) -> List[int]:
        ans = [0]

        if n == 0:
            return ans

        block = [1]
        power = 0

        while 2 ** power <= n:
            ans += block

            next_block = block + [i + 1 for i in block]
            power += 1
            block = next_block

        return ans[:n + 1]
