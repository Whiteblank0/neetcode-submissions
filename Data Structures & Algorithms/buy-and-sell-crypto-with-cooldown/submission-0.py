from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, hold):
            if i < 0:
                return 0 if not hold else float('-inf')
            if hold:
                return max(dfs(i-1, True), dfs(i-2, False) - prices[i])
            else:
                return max(dfs(i-1, False), dfs(i-1, True) + prices[i])
        
        return dfs(n-1, False)