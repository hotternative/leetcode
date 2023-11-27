class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Runtime 193 ms Beats 70.81% Memory 14.7 MB Beats 29.1%
        n = len(isConnected)
        visited = [0] * n
        result = 0

        def dfs(visited, i):
            for j in range(n):
                if isConnected[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    visited = dfs(visited, j)
            return visited

        for i in range(n):
            if not visited[i]:
                visited = dfs(visited, i)
                result += 1

        return result