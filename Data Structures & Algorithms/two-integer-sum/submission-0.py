class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                offset = target - nums[i]
                dic[offset] = i
            else:
                return [dic[nums[i]], i]