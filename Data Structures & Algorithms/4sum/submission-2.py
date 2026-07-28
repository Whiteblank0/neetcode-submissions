class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i + 1, n - 2):
                l = j + 1
                r = n - 1

                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                if nums[i] + nums[j] + nums[-2] + nums[-1] < target:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total > target:
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        result = [nums[i], nums[j], nums[l], nums[r]]
                        ans.append(result)
                        l += 1
                        r -= 1
                        
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        
        return ans