class Solution:
    def lowerbounder(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left 

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        before = self.lowerbounder(nums, target)
        if before == len(nums) or nums[before] != target:
            return [-1, -1]
        after = self.lowerbounder(nums, target + 1) - 1
        return [before, after]