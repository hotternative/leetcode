# Created on 02/02/2021
from collections import defaultdict
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) == 1:
            return adjacentPairs[0]

        d = defaultdict(set)
        for p in adjacentPairs:
            d[p[0]].add(p[1])
            d[p[1]].add(p[0])

        print(d)

        result = []
        for k, v in d.items():
            if len(v) == 1:
                result.append(k)
                break
        pre = k
        cur = v.pop()

        while True:
            cur_set = d[cur]
            if len(cur_set) == 1:
                result.append(cur)
                break
            else:
                cur_set.remove(pre)
                pre = cur
                cur = cur_set.pop()
                result.append(pre)

        return result



r = Solution.restoreArray(Solution,[[4,-2],[1,4],[-3,1]])
r = Solution.restoreArray(Solution,[[2,1],[3,4],[3,2]])
r = Solution.restoreArray(Solution,[[100000,-100000]])

print(r)
