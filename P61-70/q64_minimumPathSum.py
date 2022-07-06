class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])

        dp = [[grid[0][0] for i in range(column)] for j in range(row)]

        for i in range(1, column):
            dp[0][i] = grid[0][i] + dp[0][i-1]

        for i in range(1, row):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for i in range(1, row):
            for j in range(1, column):
                dp[i][j] = min(grid[i][j]+dp[i][j-1], grid[i][j]+dp[i-1][j])

        return dp[-1][-1]