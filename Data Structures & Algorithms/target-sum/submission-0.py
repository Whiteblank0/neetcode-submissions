class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2

        n = len(nums)
        f = [0] * (target + 1)
        f[0] = 1

        for num in nums:
            for c in range(target, num - 1, -1):
                f[c] = f[c] + f[c - num]
        return f[target]