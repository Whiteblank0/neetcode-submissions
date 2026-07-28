class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                l = j + 1
                r = n - 1

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total > target:
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        result = [nums[i], nums[j], nums[l], nums[r]]
                        if result not in ans:
                            ans.append(result)
                        l += 1
                        r -= 1
                        
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        
        return ans