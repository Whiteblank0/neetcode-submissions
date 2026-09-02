class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        target = len(nums) // 3
        res = []

        for num in nums:
            count[num] += 1
            if num not in res and count[num] > target:
               res.append(num)
        
        return res