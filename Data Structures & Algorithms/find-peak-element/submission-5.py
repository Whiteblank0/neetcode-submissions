class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 2

        while left <= right:
            m = left + (right - left) // 2
            if nums[m] < nums[m + 1]:
                left = m + 1
            else:
                right = m - 1
        
        return left