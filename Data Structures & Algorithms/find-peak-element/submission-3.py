class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            m = left + (right - left) // 2
            if m > 0 and nums[m] < nums[m - 1]:
                right = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                left = m + 1
            else:
                return m