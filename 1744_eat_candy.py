# Created on 02/02/2021
from typing import List

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:

        s_dic = {}
        def find_s(d):
            if d in s_dic:
                return s_dic[d]

            if d == 0:
                return 0
            elif d == 1:
                s_dic[d] = candiesCount[0]
                return s_dic[d]
            else:
                s_dic[d] = find_s(d-1) + candiesCount[d-1]
                return s_dic[d]

        r = []
        for q in queries:
            ft = q[0]
            fd = q[1]
            dc = q[2]

            min_eat = fd + 1
            max_eat = min_eat * dc

            s = find_s(ft)
            c1 = s < max_eat
            c2 = s + candiesCount[ft] >= min_eat

            r.append(c1 and c2)
        return r

candiesCount = [7,4,5,3,8]
queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
r = Solution.canEat(Solution, candiesCount, queries)
print(r)

candiesCount = [5,2,6,4,1]
queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
r = Solution.canEat(Solution, candiesCount, queries)
print(r)