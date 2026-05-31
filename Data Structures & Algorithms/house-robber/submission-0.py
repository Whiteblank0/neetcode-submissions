class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f0 = f1 = 0
        for i in range(n):
            new_F = max(f1, f0 + nums[i])
            f0 = f1
            f1 = new_F
        return f1