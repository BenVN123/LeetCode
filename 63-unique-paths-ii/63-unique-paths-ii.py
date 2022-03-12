class Solution:
    def uniquePathsWithObstacles(self, M):
        m, n = len(M), len(M[0])
        dp = [0] * n
        dp[0] = 1
        for i, j in product(range(m), range(n)):
            if M[i][j]: dp[j] = 0
            elif j > 0: dp[j] += dp[j - 1]
        return dp[-1]