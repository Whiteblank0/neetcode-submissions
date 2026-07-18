import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ng = 0
        for x in nums:
            j = bisect.bisect_left(nums, x, 0, ng)
            if j == ng:
                nums[ng] = x
                ng += 1
            else:
                nums[j] = x
        return ng