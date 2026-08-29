from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(2)]
        dp[(m - 1) % 2][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue

                dp[i % 2][j] = dp[(i + 1) % 2][j] + dp[i % 2][j + 1]
        
        return dp[0][0]