class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, count = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                count += 1
        
        res = [0] * len(nums)

        if count > 1:
            return res
        
        for i in range(len(nums)):
            if count:
                res[i] = 0 if nums[i] else prod
            else:
                res[i] = prod // nums[i]
        
        return res