from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs, k):
        ua = defaultdict(set)
        for log in logs:
            u, t = log
            ua[u].add(t)

        c = {}
        for u, l in ua.items():
            c[u] = len(l)

        ans = [0] * k
        for d, n in c.items():
            ans[n-1] += 1

        return ans

logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
a = Solution.findingUsersActiveMinutes(Solution, logs, k)
print(a)

logs = [[1, 1], [2, 2], [2, 3]]
k = 4
a = Solution.findingUsersActiveMinutes(Solution, logs, k)
print(a)
