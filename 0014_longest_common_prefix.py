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
