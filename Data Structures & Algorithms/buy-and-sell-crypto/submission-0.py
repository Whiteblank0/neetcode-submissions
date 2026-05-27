class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minmum = float('inf')
        profit = 0

        for price in prices:
            if price - minmum > profit:
                profit = price - minmum
            if price < minmum:
                minmum = price
        
        return profit