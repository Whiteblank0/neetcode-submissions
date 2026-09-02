class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, curMin = 0, 0
        gloMax, gloMin = nums[0], nums[0]
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            gloMax = max(gloMax, curMax)
            gloMin = min(gloMin, curMin)
        
        return max(gloMax, total - gloMin) if gloMax > 0 else gloMax