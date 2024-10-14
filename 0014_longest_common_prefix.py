# 15 Dec 2022
# Runtime 43 ms Beats 81.43% Memory 14 MB Beats 50.3%

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cs = strs[0]
        for s in strs[1:]:
            new_common_str = ""
            for i, c in enumerate(cs):
                if i >= len(s):
                    cs = new_common_str
                    break

                if s[i] == c:
                    new_common_str += c
                else:
                    cs = new_common_str
                    break
            else:
                cs = new_common_str
        return cs


class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pointer = 0
        leading_str = strs[0]

        while pointer < len(leading_str):
            for s in strs:
                if s[pointer] != leading_str[pointer]:
                    return leading_str[0:pointer]
            else:
                pointer += 1



if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    assert Solution2.longestCommonPrefix(Solution2(), strs) == "fl"
