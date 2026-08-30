from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i, total):
            if total == amount:
                return 1
            if total > amount or i == len(coins):
                return 0
            
            return dfs(i, total + coins[i]) + dfs(i + 1, total)
        
        return dfs(0, 0)