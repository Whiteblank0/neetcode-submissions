from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        @cache
        def dfs(total):
            if total == amount:
                return 0

            if total > amount:
                return float('inf')
            
            return min(1 + dfs(c + total) for c in coins)
        
        res = dfs(0)
        return res if res != float('inf') else -1